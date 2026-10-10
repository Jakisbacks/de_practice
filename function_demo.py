def get_discount_percent(amount):
    if amount >= 1000:
        return 20
    elif amount >= 500:
        return 10
    else:
        return 0


amounts = [1200,700,300]

for amount in amounts:
    discount_percent = get_discount_percent(amount)
    final_amount = amount - amount * discount_percent / 100
    print("Order:", amount, "| Final:", final_amount)
