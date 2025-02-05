def greet(name = "User"):  #if parameter is not passed then it use the default value  "user"
    return "hello "+ name +"!"

print(greet("chai"))
print(greet())