import pandas as pd

# Series 單維度
phone = pd.Series(["Apple", "Samsung", "Mi", "Sony"], index=["p1", "p2", "p3", "p4"])
# print(phone[1])
# print(phone["p3"])

other_phone = pd.Series(["Htc", "Oppo"])
# combined = phone.append(other_phone, ignore_index=True)
combined = pd.concat([phone, other_phone], ignore_index=True)

combined[1] = 'new_Samsung'
# print(combined)
# print(combined.size) # 取得Pandas Series資料筆數
# print(combined.str.upper()) # 將字串轉為大寫
# print(combined.str.contains("Sa")) # 搜尋是否包含特定字串
# print(combined.str.cat(sep=';')) # 利用自訂的分隔符號連接字串
# print(combined.str.replace("Samsung", "Oppo"))  # 將Samsung取代為Oppo

numbers = pd.Series([22, 5, 10, 12, 6, 30])
# print(numbers.max())
# print(numbers.min())
# print(numbers.sum())
# print(numbers.mean())
# print(numbers.nlargetst(2)) # 最大的n個數值
# print(numbers.nsmallest(2))  # 最小的2個數值

