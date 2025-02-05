pet_species = input("provide the species of the pet:")
age = int (input("provide me the age of your pet: "))
if (pet_species == "dog" and age < 2):
    pet_food = "puppy food"
elif (pet_species == "dog" and age > 2):
    pet_food = "pedigrie"
elif (pet_species == "cat" and age < 5):
    pet_food = "junior cat food"
elif(pet_species == "dog" and age > 5):
    pet_food = "senior cat food"
else:
    pet_food = "we will recommend you later after further study"

print("the recommended pet food is: ",pet_food)