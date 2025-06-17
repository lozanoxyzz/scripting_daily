import csv

people = [
    ['Dan', 34, 'Bucharest'],
    ['Andrei', 21, 'London'],
    ['Maria', 45, 'Paris']
]

with open('results/people1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',)
    for row in people:
        writer.writerow(row)

with open("results/people1.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)