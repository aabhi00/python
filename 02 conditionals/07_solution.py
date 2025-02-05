order_size = input("provide me the size of the coffee: ")
extra_shot = True
if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"
print("order: ",coffee)