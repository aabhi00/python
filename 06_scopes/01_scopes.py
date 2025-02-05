username = "codeaurchai"

def user():
    print(username)

x = 99
def func(y):
    x = 8
    z = x + y
    return z

result = func(4)
print(result)

def func2():
    print(x)

func2()

def chaicode(num):
    def actual(x):
        return x ** num
    return actual

f = chaicode(2)
g = chaicode(3)

print(f(3))
print(g(3))
