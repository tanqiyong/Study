# a, b = 0, 1
# for i in range(6):
#     print(a)
#     a, b = b, a+b

import pandas as pd

# data = pd.read_excel("test.xlsx")
# print(data)
# print(data.tail(1))
# data = {"姓名": ["a", "b", "c"], "年龄": [1, 2, 3]}
# print(data)
# df = pd.DataFrame(data)
# print(df)
# print(type(data))
# print(type(df))
# df.to_excel("t1.xlsx")

#
# data1 = pd.read_excel("t1.xlsx", header=1)
# data2 = pd.read_excel("t2.xlsx", header=1)
# data = pd.concat([data1, data2])
# data.to_excel("sum.xlsx", index=False, sheet_name="表一")

import os
data = pd.read_excel("t.xlsx", header=1)
entries = os.scandir("./")
# print(entries)
for entry in entries:
    if entry.name.endswith("xlsx"):
        print(entry.name)
        data1 = pd.read_excel(entry, header=1)
        data = pd.concat([data1, data])
data.to_excel("sum.xlsx", index=False, sheet_name="表一")



