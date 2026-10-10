import csv

with open("orders.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)