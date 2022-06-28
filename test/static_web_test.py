from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
import time
import datetime
import requests
import re
from bs4 import BeautifulSoup as bf
import os
import shutil


def url_parse_test():
    url = 'https://www.youtube.com/watch?v=ceUhb2-gYOU&=123'
    url_obj = urlparse(url)
    print(url_obj)
    print('scheme={}'.format(url_obj.scheme))
    print('netloc={}'.format(url_obj.netloc))
    print('port={}'.format(url_obj.port))
    print('path={}'.format(url_obj.path))
    print('query={}'.format(url_obj.query))


def start_browser():
    options = Options()
    options.add_argument("--disable-notifications")  # 取消網頁中的彈出視窗

    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=options)
    browser.get("https://www.facebook.com/")

def request_test():
    url = 'https://www.taiwanlottery.com.tw/lotto/Lotto649/history.aspx'
    html = requests.get(url)
    html.encoding = 'utf-8'
    # html_list = html.text.splitlines()
    sp = bf(html.text, 'html.parser')
    # print(sp.title) #傳回網頁標題
    # print(sp.text) #去除所有HTML標籤的文字內容
    print(sp.find('td', {'class':'td_w font_black14b_center'})) #傳回第一個符合條件的tag
    print(sp.find('td', {'class':'td_w font_black14b_center'}).text)
    print(sp.find_all('td', {'class':'td_w font_black14b_center'})) #傳回所有符合條件的tag
    print(sp.find('td', {'class':'td_w font_black14b_center'}).get('width')) #傳回屬性內容

    print(sp.select('.td_org1')[0].text) #傳回指定CSS選擇器如id或class的內容

def regex_test():
    str_test = '021ddf,asd90'
    pat = re.compile('[a-z]+')
    sar = pat.search(str_test) #從string中搜尋
    print(sar.group()) #ddf
    print(sar.start()) #3
    print(sar.end()) #6
    print(sar.span()) #(3, 6)

    mat = pat.match(str_test)
    print(mat) #None 匹配string開頭

    mat2 = re.match(r'[a-z]+', 'temp321')
    print(mat2.group())

    list1 = pat.findall(str_test)
    print(list1)

    print('============')
    content = '33STR123TRE66PPP009'
    regex = r'[A-Z]+\d'
    sear2 = re.search(regex, content)
    # print(sear2.group(), sear2.group(0), sear2.group(1), sear2.group(2))
    print(re.findall(r'([A-Z]+(\d))', content)) #[('STR1', '1'), ('TRE6', '6'), ('PPP0', '0')]
    print(re.findall(r'[A-Z]+\d', content)) #['STR1', 'TRE6', 'PPP0']
    print(re.findall(r'[A-Z]+(\d)', content)) #['1', '6', '0']

def get_number_test():
    html = requests.get('https://www.taiwanlottery.com.tw/index_new.aspx')
    html.encoding = 'utf-8'
    sp = bf(html.text, 'html.parser')
    data1 = sp.select('#rightdown')
    data2 = data1[0].find('div', {'class':'contents_box02'})
    data3 = data2.find_all('div', {'class':'ball_tx'})
    print(data3)
    print('開獎號碼: ')
    for i in range(6):
        print(data3[i].text, end=' ')

    print('\n第二區號碼: ')
    data4 = data2.find('div', {'class':'ball_red'})
    print(data4.text)

def time_test():
    print(datetime.datetime.now())
    print(datetime.date.today()) #2022-02-01
    tonow = datetime.datetime.now()
    print(tonow.year)
    print(tonow.month)
    print(tonow.day)

    dt = datetime.datetime.strptime('20220101', "%Y%m%d") # string to date
    st_str = dt.strftime("%Y_%m_%d %H:%M:%S")# date to string
    print(dt)
    print(st_str)

def get_pic_download():
    dir_name = 'ig_pic2'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    html = requests.get('http://www.tatyun.com/p/1V5348')
    html.encoding = 'utf-8'
    sp = bf(html.text, 'html.parser')

    data1 = sp.find('div', {'class', 'contentL left article'}).find_all('img', {'class', 'lazy bimg'})
    links = []
    for link in data1:
        links.append(link.get('data-original'))

    # links = sp.select('.contentL .lazy.bimg')
    # print(links[0])

    for link in links:
        print(link)
        file_name = link.split('/')[-1]
        try:
            image = requests.get(link, stream=True)
            with open(os.path.join(dir_name, file_name), 'wb') as f:
                shutil.copyfileobj(image.raw, f)
        except:
            print('{}無法讀取'.format(file_name))

if __name__ == '__main__':
    get_pic_download()
    # request_test()
