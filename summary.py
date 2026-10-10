orders = [
    {"order_id": 1, "city": "Delhi", "amount": 1200},
    {"order_id": 2, "city": "Mumbai", "amount": 700},
    {"order_id": 3, "city": "Delhi", "amount": 300},
]

total = 0
delhi_count = 0

for order in orders:
    total += order["amount"]

    if order["city"] == "Delhi":
        delhi_count += 1

print("Total:", total)
print("Delhi orders:", delhi_count)