# tiers program
amount = int(input("Order amount: "))

if amount >= 1000:
    discount_percent = 20
elif amount >= 500:
    discount_percent = 10
else:

discount_amount = amount * discount_percent / 100
final_amount = amount - discount_amount
print("Discount:",discount_percent,"%")
print("Discount amount:",discount_amount)
print("Final amount:",final_amount)