import json
from import Parse

message = Parse(json.dumps({
    "first": "a string",
    "second": True,
    "third": 123456789
}), Thing())

print(message.first)  # "a string"
print(message.second) # True
print(message.third)  # 123456789
