import csv

good_rows = []
bad_rows = []

with open("dirty_orders.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            row["amount"] = int(row["amount"])
            good_rows.append(row)
        except (ValueError,TypeError):
            bad_rows.append(row)

with open("clean_orders.csv", "w", newline="") as out_file:
    writer = csv.DictWriter(out_file, fieldnames=["order_id","city","amount"])
    writer.writeheader()
    writer.writerows(good_rows)

with open("rejected_orders.csv", "w", newline="") as bad_file:
    bad_writer = csv.DictWriter(bad_file, fieldnames=["order_id", "city", "amount"])
    bad_writer.writeheader()
    bad_writer.writerows(bad_rows)

print("Clean rows:", len(good_rows))
print("Bad rows:", len(bad_rows))
