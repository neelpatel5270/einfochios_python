import json

data = {
    "cava":"springboot",
    "bode":"express.js",
    "automation":"py"
}

print(json.dumps(data, indent=4, sort_keys="True"))
