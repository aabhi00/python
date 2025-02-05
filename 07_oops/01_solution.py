class car: 
    total_car = 0                 # class
      
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        car.total_car += 1
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
       
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def general_description():
        return "cars are means of transport"
    
    @property
    def model(self):
        return self.__model + " !"
    

class ElectricCar(car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "electric charge"

# my_car = car("toyota", "corolla") #object
# # my_car.model = "city"
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.full_name())


# my_new_car = car("tata", "safari")  #object
# print(my_new_car.get_brand())
# print(my_new_car.model)
# print(my_new_car.full_name())
# print(my_new_car.fuel_type())
# print(car.general_description())


# print(my_car.model)

my_tesla = ElectricCar("tesla","model S","85KWWh")
print(isinstance(my_tesla,car))
print(isinstance(my_tesla,ElectricCar))

# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.fuel_type()) #polymorphism as in both the cases the it has same definition name but it gives different values for electric and petrol cars
# print(car.total_car)

class battery:
    def battery_info(self):
        return "this is battery"

class engine:
    def engine_info(self):
        return "ths is engine"

class electricCarTwo(battery,engine,car):
    pass
my_new_tesla = electricCarTwo("tesla","model S")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())