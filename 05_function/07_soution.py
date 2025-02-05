def sum_all(*args):
    print(args) # gives us tuple
    print(*args)
    return sum(args) #inbuilt function sum which will sum all the values in the args

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8))