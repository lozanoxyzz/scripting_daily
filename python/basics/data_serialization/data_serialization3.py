import requests
import json
import csv

r = requests.get("https://jsonplaceholder.typicode.com/users")

python_object = json.loads(r.text)

result_list = []


for row in python_object:
    user_list = []
    user_list.append(row["name"])
    user_list.append(row["address"]["city"])
    user_list.append(row["address"]["geo"])
    user_list.append(row["company"]["name"])
    result_list.append(user_list)

print(result_list)

with open("results/users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(result_list)