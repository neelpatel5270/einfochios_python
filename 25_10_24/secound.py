import json
sampleJson = """{ "java":"springboot","node":"express.js"}"""

finaljshon=json.loads(sampleJson)

print(finaljshon["node"])