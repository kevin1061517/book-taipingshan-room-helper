import pandas
import requests
from bs4 import BeautifulSoup
import json
import datetime
import time
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


def get_stock_data(stock_num):
    now_ymd = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    url = f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date={now_ymd}&stockNo={stock_num}' \
          f'&_={str(time.mktime(datetime.datetime.now().timetuple()))}'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    stock_data = json.loads(soup.text)

    if stock_data['stat'] == 'OK':
        return [stock_data['data']]

    return []


# https://www.twse.com.tw/zh/trading/historical/stock-day-avg.html
def standard_analyze(stock_num):
    stock_list = get_stock_data(stock_num)
    if len(stock_list) == 0:
        print('Check stock number')
        return

    stock_df = pd.DataFrame(stock_list[0],
                            columns=['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差',
                                     '成交筆數'])
    stock_average = pd.to_numeric(stock_df['收盤價']).mean()
    stock_STD = pd.to_numeric(stock_df['收盤價']).std()

    # check stock price
    result = 'Stock price is too expensive'
    if pd.to_numeric(stock_df['收盤價'][-1:]).values[0] < stock_average - (2 * stock_STD):
        result = 'Stock price is acceptable'

    print(f'收盤價={stock_df["收盤價"][-1:].values[0]}\n中間價={str(stock_average)}\n線距={str(stock_STD)}')
    print('Result: ' + result)


# https://goodinfo.tw/tw/StockBzPerformance.asp?STOCK_ID=2303&RPT_CAT=M%5FYEAR
def get_performance_analysis(stock_num):
    url = 'https://goodinfo.tw/tw/StockBzPerformance.asp?STOCK_ID=2303&RPT_CAT=M%5FYEAR'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    performance_form_html = soup.select_one('#divDetail').prettify()

    df = pandas.read_html(performance_form_html)[0]
    # 只要保留兩層的最後一層那一列就好
    df.columns = df.columns.get_level_values(1)
    print(df.head())
    return df.head()


if __name__ == '__main__':
    # standard_analyze('2303')
    get_performance_analysis('2303')
