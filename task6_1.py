import json

dictionary = {"id": "04", "name": "Vladislav", "department": "HR"} 

dictionary_to_json = json.dumps(dictionary, indent = 4)

print(dictionary_to_json)