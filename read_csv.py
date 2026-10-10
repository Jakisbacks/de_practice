import csv

total = 0
delhi_total = 0
with open("orders.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        amount = int(row["amount"])
        total += amount
        if row["city"] == "Delhi":
            delhi_total += amount

print("Total:",total)
print("Delhi Total amount:",delhi_total)


with open("summary.txt","w") as out_file:
    out_file.write("Total: " + str(total) + "\n")
    out_file.write("Delhi Total amount: " + str(delhi_total) + "\n")