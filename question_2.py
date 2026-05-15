import re

print("请输入文本（双击回车结束）：")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
text = "\n".join(lines)


def reg_search(text, regex_list):
    results = []

    for rule in regex_list:
        item_result = {}

        for key, pattern in rule.items():
            match = re.findall(pattern, text)
            item_result[key] = match

        results.append(item_result)

    return results

regex_list = [{
    '标的证券': r'\d{6}\.\w+',
    '换股期限': r'(\d{4})\s*年\s*(\d{1,2})\s*月\s*(\d{1,2})\s*日'
}]
#打印出来的日期不符合要求，我们用循环判断的方法进行格式转换
result = reg_search(text, regex_list)
for record in result:
    for field_name, field_value in record.items():
        if isinstance(field_value, list) and field_value and isinstance(field_value[0], tuple):
            dates = []
            for m in field_value:
                date_str = f"{m[0]}-{int(m[1]):02d}-{int(m[2]):02d}"
                dates.append(date_str)
            print(f"{field_name}: {dates}")
        elif isinstance(field_value, list) and len(field_value) == 1:
            print(f"{field_name}: {field_value[0]}")
        else:
            print(f"{field_name}: {field_value}")
