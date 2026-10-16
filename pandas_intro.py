import pandas as pd

df = pd.read_csv("dirty_orders.csv")

print(df["amount"])

df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

print(df)
print(df.dtypes)