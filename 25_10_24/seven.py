import json

# Sample JSON data
data = """[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

datone=json.loads(data)
list1 = []
for i in datone:
    list1.append(i["name"])

print(list1)

