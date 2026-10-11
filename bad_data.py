amounts = ["250", "400", "abc", "150"]
total = 0

for value in amounts:
    try:
        total += int(value)
    except ValueError:
        print("Wrong Value detected:", value)

print("Total:",total)