import csv

def extract(path):
    with open(path) as file:
        return list(csv.DictReader(file))

def transform(rows):
    good = []
    bad = []

    for row in rows:
        try:
            row["amount"] = int(row["amount"])
            good.append(row)
        except (ValueError, TypeError):
            bad.append(row)
    return good, bad

def load(rows, path):
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["order_id", "city", "amount"])
        writer.writeheader()
        writer.writerows(rows)

raw_rows = extract("dirty_orders.csv")
good_rows, bad_rows = transform(raw_rows)
load(good_rows, "clean_orders.csv")
load(bad_rows, "rejected_orders.csv")

print("Clean rows:", len(good_rows))
print("Bad rows:", len(bad_rows))