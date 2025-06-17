import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

python_object = json.loads(r.text)
print(python_object)

for row in python_object:
    if row["completed"] == True:
        print(row)