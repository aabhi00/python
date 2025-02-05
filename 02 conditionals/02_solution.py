age = int(input("provide me the age : "))
day = input("provide what is the day today: ")

price = 12 if age >= 18 else 8
if day == "wednesday":
    price -= 2
print("ticket price for you is $",price)

