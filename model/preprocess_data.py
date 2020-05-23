import json

with open("data/annotations.json", "r") as rf:
    data = json.loads(rf.read())

print(data["annotations"][1])