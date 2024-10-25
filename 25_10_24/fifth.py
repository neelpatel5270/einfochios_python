import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

newdata= json.loads(sampleJson)
sundata = newdata["company"]["employee"]["payble"]["salary"]
print(sundata)
