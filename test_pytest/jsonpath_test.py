import json

import jsonpath
import yaml

with open("./data/data.yml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)

print(datas)
print(type(datas))  # dict 字典
print(datas['add']['P0']['datas'])  # [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]]
print(datas['add']['P0']['ids'])  # ['2个整数', '2个浮点数', '整数+浮点数']

data_jsonpath = jsonpath.jsonpath(datas, '$..P0.datas')
print(data_jsonpath)  # [[[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]]]
# data_2 = []
# for data in data_jsonpath:
#     data_2 = data
# print(data_2)  # [[1, 1, 2], [-0.01, 0.02, 0.01], [10, 0.02, 10.02]]

# json.dumps()将Python dict数据结构转换为JSON （json是字符串）
json_data = json.dumps(datas)
print(json_data)
print(type(json_data))  # str 字符串

