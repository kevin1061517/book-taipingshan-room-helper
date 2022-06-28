import pandas as pd

grades = {
    "name": ["Mike", "Sherry", "Cindy", "John"],
    "math": [80, 75, 93, 86],
    "chinese": [63, 90, 85, 70]
}
df = pd.DataFrame(grades)

# print("取得資料索引值為1和3的name及chinese欄位資料集")
# print(df.loc[[1, 3], ["name", "chinese"]])

# print("取得資料索引值為1和3的第一個及第三個欄位資料集")
# print(df.iloc[[1, 3], [0, 2]])

# new_df = df.drop(["math"], axis=1) #axis為1表示砍掉欄
# print("刪除math欄位")
# print(new_df)

# new_df = df.drop([0, 3], axis=0)  # axis為0表示砍掉列 刪除第一筆及第四筆資料
# print("刪除第一筆及第四筆資料")
# print(new_df)

# df = df.append({"name": "kevin", "math": 56, "chinese":70}, ignore_index=True)

# df2 = pd.DataFrame(
#     columns=["name", "math", "chinese"],
#     data=[["Mike", 80, 63], ["Sherry", 75, 90], ["Cindy", 93, 85]]
# )

# grades = [
#     ["Mike", 80, 63],
#     ["Sherry", 75, 90],
#     ["Cindy", 93, 85],
#     ["John", 86, 70]
# ]
# new_df = pd.DataFrame(grades)
# print("使用陣列來建立df：")
# print(new_df)

# df.index = ["s1", "s2", "s3", "s4"]  #自訂索引值
# df.columns = ["student_name", "math_score", "chinese_score"]  #自訂欄位名稱
# new_df = df.head(2) # 取得最前面的兩筆資料
# new_tail_df = df.tail(3) # 取得最後面的三筆資料

# df2 = pd.DataFrame({
#     "name": ["Henry"],
#     "math": [60],
#     "chinese": [62]
# })
#
# new_df = pd.concat([df, df2], ignore_index=True)
# print("合併df來新增資料")
# print(new_df)


