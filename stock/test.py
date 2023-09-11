import pandas as pd
import datetime


# s = '第 1 / 100 頁'
# first_page = s[2:s.index('/')].strip()
# last_page = s[s.index('/')+1:-1].strip()
# print(int(first_page)+1)
# print(last_page)
#
# df = pd.DataFrame([{'name': 'kevin', 'age': 18}, {'name': 'Kent', 'age': 22}])
# print(df)
# df.to_excel('jobs_vacancy_data.xlsx', index=False)




dt = datetime.datetime.strptime('20230730', "%Y%m%d")
s = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=5), '%m%d')
print(datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d'))
