import csv


csv.register_dialect("colon", delimiter=":", quoting=csv.QUOTE_NONE, lineterminator="\n")

with open("../../media/devices.txt", "r") as csvfile:
    reader = csv.reader(csvfile, dialect="colon")
    for row in reader:
        print(row)