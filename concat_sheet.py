import pandas as pd
import os
data = pd.read_excel("t.xlsx", header=1)
entries = os.scandir("./")
# print(entries)
for entry in entries:
    if entry.name.endswith("xlsx"):
        print(entry.name)
        data1 = pd.read_excel(entry, header=1)
        data = pd.concat([data1, data])
data.to_excel("汇总表.xlsx", index=False, sheet_name="表一")

