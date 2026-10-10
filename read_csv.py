import csv

total = 0

with open("orders.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += int(row["amount"])

print("Total:",total)