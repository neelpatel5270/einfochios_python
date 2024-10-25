import json

data = {
    "java":"springboot",
    "node":"express.js"
}

finaldata= json.dumps(data, indent=4, separators=(". "," = "))
print(finaldata)