from pipeline import extract

rows = extract("dirty_orders.csv")
print("Rows:", len(rows))