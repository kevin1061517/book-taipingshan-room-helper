import pandas as pd
import requests
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


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


if __name__ == '__main__':
    df_companies_jobs = get_company_jobs_details()
    print(df_companies_jobs)
    df_companies_jobs.to_csv('companies_jobs_data.csv', index=False, encoding='utf-8-sig')
