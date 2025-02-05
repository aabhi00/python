distance = int(input("provide me the distace you have to travel: "))

if distance  <= 3:
    transport = "walk"
elif distance <= 15:
    transport = "bike"
else:
    transport = "car"

print("AI recommends you the transport of:",transport)