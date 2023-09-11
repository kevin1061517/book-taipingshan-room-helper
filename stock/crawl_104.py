import pandas as pd
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import datetime

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# This function retrieves job vacancy data for listed and over-the-counter (OTC) companies
def get_company_jobs_details():
    url = 'https://www.104.com.tw/company/ajax/list?zone=16&jobsource=cs_sub_custlist&mode=s&page={}&pageSize=18'
    headers = {'Referer': 'https://www.104.com.tw/company/search/?zone=16&jobsource=cs_sub_custlist&mode=s&page=1'}

    resp = requests.get(url.format(1), headers=headers)
    content_json = json.loads(resp.text)
    last_page = content_json['metadata']['pagination']['lastPage']
    print(f'Total Page: {last_page}')

    df_all_company_job = pd.DataFrame()
    for curr_page in range(1, last_page + 1):
        print(f'Progress Company.. current page: {curr_page}')
        curr_resp = requests.get(url.format(curr_page), headers=headers)
        curr_company_json = json.loads(curr_resp.text)

        df_company = pd.DataFrame(data=curr_company_json['data'],
                                  columns=['encodedCustNo', 'name', 'jobCount', 'employeeCountDesc'])
        df_job = get_jobs_details_by_company_json(curr_company_json['data'])
        df_company_job = pd.merge(df_company, df_job, how="outer")
        df_all_company_job = pd.concat([df_all_company_job, df_company_job], ignore_index=True)

    df_all_company_job = df_all_company_job.rename(
        {'encodedCustNo': 'company_id', 'employeeCountDesc': 'employee_count'}, axis=1)
    df_all_company_job.sort_values(by=['company_id'], ascending=False)
    return df_all_company_job


def get_jobs_details_by_company_json(curr_company_json):
    if curr_company_json is None:
        return

    df_all_job = pd.DataFrame()
    for company in curr_company_json:
        curr_company_id = company['encodedCustNo']
        df_jobs = pd.DataFrame([{'encodedCustNo': curr_company_id}])
        job_count = company['jobCount']
        if job_count != 0:
            df_jobs = get_jobs_details_by_company_id(curr_company_id)
        df_all_job = pd.concat([df_all_job, df_jobs], ignore_index=True)

    return df_all_job


def get_jobs_details_by_company_id(company_id):
    url = f'https://www.104.com.tw/company/ajax/joblist/{company_id}'
    headers = {'Referer': url}

    resp = requests.get(url, headers=headers)
    content_json = json.loads(resp.text)
    total_pages = content_json['data']['totalPages']
    print(f'Company Id: {company_id}, Total Page: {total_pages}')

    url += '?page={}'
    df_all_job = pd.DataFrame()
    for curr_page in range(1, total_pages + 1):
        print(f'Progress Job.. current page: {curr_page}')
        curr_resp = requests.get(url.format(curr_page), headers=headers)
        curr_company_json = json.loads(curr_resp.text)

        # analysisType => 1=0~5 / 2=6~10 / 3=11~30...
        df_job = pd.DataFrame(data=curr_company_json['data']['list']['normalJobs'],
                              columns=['encodedJobNo', 'jobName', 'appearDate', 'analysisType'])
        df_all_job = pd.concat([df_all_job, df_job], ignore_index=True)

    df_all_job = df_all_job.rename(
        {'encodedJobNo': 'job_id', 'appearDate': 'update_date', 'analysisType': 'apply_popularity'}, axis=1)
    df_all_job['encodedCustNo'] = company_id

    return df_all_job


def get_job_vacancy(keyword, update_days_before_now, over_salary=None):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    params = {'keyword': keyword, 'isnew': update_days_before_now,
              'mode': 'l', 'ro': '1'}
    if over_salary is not None:
        params['sctp'] = 'M'
        params['scmin'] = over_salary
    resp = requests.get('https://www.104.com.tw/jobs/search', params, headers=headers)

    driver = webdriver.Chrome()
    driver.get(resp.url)
    page_info = driver.find_element(By.CSS_SELECTOR,
                                    ".b-clear-border.page-select.js-paging-select.gtm-paging-bottom option").text
    curr_page = int(page_info[2:page_info.index('/')].strip())
    last_page = int(page_info[page_info.index('/') + 1:-1].strip())
    print(f'current page: {curr_page} / Last Page: {last_page}')

    job_list = pd.DataFrame()
    # driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    while True:
        job_array = driver.find_elements(By.CSS_SELECTOR, ".job-mode.js-job-item")
        for job in job_array:
            company_name = job.get_attribute('data-cust-name')
            job_title = job.get_attribute('data-job-name')
            job_city = job.find_element(By.CSS_SELECTOR, '.job-mode__area').text
            job_academy = job.find_element(By.CSS_SELECTOR, '.job-mode__edu').text
            job_experience = job.find_element(By.CSS_SELECTOR, '.job-mode__exp').text
            job_link = job.find_element(By.CSS_SELECTOR, '.job-mode__jobname a').get_attribute('href')

            df = pd.DataFrame(
                data=[{
                    '公司名稱': company_name,
                    '工作職稱': job_title,
                    '上班地點': job_city,
                    '學歷要求': job_academy,
                    '工作經歷': job_experience,
                    '連結路徑': job_link}],
                columns=['公司名稱', '工作職稱', '上班地點', '學歷要求', '工作經歷', '連結路徑'])
            job_list = pd.concat([job_list, df], ignore_index=True)
        curr_page += 1

        resp = requests.get('https://www.104.com.tw/jobs/search?page=' + str(curr_page), params, headers=headers)
        driver.get(resp.url)
        time.sleep(1)
        if curr_page > last_page:
            break

    print('Finish crawling')
    return job_list


if __name__ == '__main__':
    job_list_result = get_job_vacancy('Java工程師', 7, 180000)
    job_list_result.to_excel('files/jobs_vacancy_data.xlsx', index=False)

    # df_companies_jobs = get_company_jobs_details()
    # print(df_companies_jobs)
    # df_companies_jobs.to_csv('files/companies_jobs_data.csv', index=False, encoding='utf-8-sig')
