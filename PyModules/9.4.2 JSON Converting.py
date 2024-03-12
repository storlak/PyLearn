# converting Json to python
import json

json_str = """
{
    "name": "Eric Smith",
    "age": 32,
    "phoneNumbers": [
        {
            "type": "home",
            "number": "(212) 555-3276"
        },
        {
            "type": "work",
            "number": "(332) 555-1234"
        }
    ],
    "spouse": null,
    "children": [],
    "employed": true
}
"""
# converting json to python: serialization
eric = json.loads(json_str)
print(eric)
# deserialization
jason_str_2 = json.dumps(eric)
print(jason_str_2)
print(json.dumps(eric, indent=2))  # indentation of 2
