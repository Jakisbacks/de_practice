# tiers program
amount = int(input("Order amount: "))

if amount >= 1000:
    print("20% discount")
elif amount >= 500:
    print("10% discount")
else:
    print("No discount")