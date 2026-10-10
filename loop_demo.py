amounts = [1200,700,300]

for amount in amounts:
    if amount >= 1000:
        discount_percent = 20
    elif amount >= 500:
        discount_percent = 10
    else:
        discount_percent = 0

    final_amount = amount - amount * discount_percent / 100
    print("Order:",amount,"| Final:",final_amount)
