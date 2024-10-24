import json

# data = {
#     "name":"Neel",
#     "age":23,
#     "city": "Ahmedabad"
# }

# newdata = json.dumps(data)
# print(data)

# jsondatasort= json.dumps(data, sort_keys=True)
# print(jsondatasort)

data3 = '{"name":"neel","collage":"charusat"}'
print(data3)

jsondata3 = json.loads(data3)
print(jsondata3)

print(type(jsondata3))