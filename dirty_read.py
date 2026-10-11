import csv

total = 0
good_rows = 0
bad_rows = 0

with open("dirty_orders.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            total += int(row["amount"])
            good_rows += 1
        except ValueError:
            bad_rows += 1
            print("Bad row, order_id:", row["order_id"])

print("Total:", total)
print("Good rows:",good_rows)
print("Bad rows:",bad_rows)