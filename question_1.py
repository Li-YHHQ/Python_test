import requests
import pandas as pd

url = "https://www.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
}

all_results = []

for page in range(1, 9):  # 因为网页中一共八页，所以我们循环八次
    data = {
        "pageNo": page,
        "pageSize": 15,
        "bondType": "100001",
        "issueYear": "2023"
    }
    response = requests.post(url, data=data, headers=headers)
    result_list = response.json()["data"]["resultList"]
    all_results.extend(result_list)
    print(f"第{page}页完成，总共{len(all_results)}条")

print(f"总共获取：{len(all_results)}条")

# 题目中不需要所有数据，所以我们提取出我们需要的数据
result = []
for item in all_results:
    result.append({
        "ISIN": item["isin"],
        "Bond Code": item["bondCode"],
        "Issuer": item["entyFullName"],
        "Bond Type": item["bondType"],
        "Issue Date": item["issueStartDate"],
        "Latest Rating": item["debtRtng"]
    })

# 已经取出数据，保存成csv
df = pd.DataFrame(result)
df.to_csv("date.csv", index=False, encoding="utf-8-sig")
print("CSV保存成功！")