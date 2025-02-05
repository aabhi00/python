def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name ="shaktiman", power = "laser")
print_kwargs(name ="shaktiman")
print_kwargs( power = "laser")
print_kwargs(name ="shaktiman", power = "laser")
print_kwargs(name ="shaktiman", power = "laser",enemy = "Dr. jackal")