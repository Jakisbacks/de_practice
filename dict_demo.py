"""order = {"order_id": 1, "city": "Delhi", "amount":250}

print(order)
print(order["city"])
print(order["amount"] + 40)"""

# creating orders_list

orders = [
    {"order_id": 1, "city": "Delhi", "amount": 1200},
    {"order_id": 2, "city": "Mumbai", "amount": 700},
    {"order_id": 3, "city": "Delhi", "amount": 300},
]

for order in orders:
    print(order["order_id"], order["city"], order["amount"])