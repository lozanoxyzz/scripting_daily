import json

friends = {"Dan": [20, "London", 3234342], "Maria": [25, "Madrid", 43525222]}

with open("results/friends.json", "w") as jsonfile:
    json.dump(friends, jsonfile)

print(json.dumps(friends, indent=4))

with open("results/friends.json", "r") as jsonfile:
    obj = json.load(jsonfile)
    print(obj)

json_string = """{
    "Dan": [
        20,
        "London",
        3234342
    ],
    "Maria": [
        25,
        "Madrid",
        43525222
    ]
}
"""

json_object = json.loads(json_string)
print(json_object)
print(type(json_object))