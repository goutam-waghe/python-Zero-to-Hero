# function

def greet(name):
    print("Hello, " + name + "!")

greet("Amit")

# function with variable

def add(a, b):
    return a + b

res = add(3, 5)
print(res)  # 8


# multiple variable 

def calculate(a, b):
    sum_ = a + b
    diff = a - b
    prod = a * b
    return sum_, diff, prod

s, d, p = calculate(10, 4)
print("Sum:", s)    # Sum: 14
print("Diff:", d)   # Diff: 6
print("Prod:", p)   # Prod: 40



# nested function

def outer(x):
    def inner(y):
        return y * y
    result = inner(x) + 10
    return result

print(outer(5))


def square(x):
    return x * x

def operate(func, value):
    return func(value)

print(operate(square, 7))

# return function from function

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(5))  # 15

times5 = make_multiplier(5)
print(times5(4))  # 20

# Formal arguments (parameters): function definition me jo names likhe hote hain.
# Actual arguments: function call karte waqt jo values pass hoti hain.
def add(a, b):  # a, b = formal arguments
    return a + b

x = 10
y = 20
print(add(x, y))  # x, y = actual arguments


# keywords

def info(name, age, city):
    print(f"{name} lives in {city} and is {age} years old.")

info(age=30, city="Mumbai", name="Rohit")
# Rohit lives in Mumbai and is 30 years old.



# default argument
def greet(name, msg="Namaste"):
    print(msg + ", " + name + "!")

greet("Anu")             # msg default --> "Namaste"
greet("Anu", "Hello")    # msg = "Hello"



def fun_positional(*args):
    print(type(args))

    total = 0
    for num in args:
        print(num)
    return total

print(fun_positional(1, 2, "str", 4))  
# args tuple: (1,2,3,4)  
# output: 10



# Jab hum nahi jaante ki function me kitne named (keyword) arguments 
# aayenge, tab **kwargs use karte hain.

# Yeh sab arguments ko ek dictionary ke form me le leta hai.
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_info(name="Amit", age=22, city="Delhi")

# lamda function
square = lambda x: x + 2
print(square(5))  

# nested lamda function
nested = lambda x: (lambda y: x + y)
print(nested)
add_five = nested(5)
print(add_five(10))  # Output: 15

# Passing Lambda Function to Another Function
def apply_func(func, value):
    return func(value)

result = apply_func(lambda x: x * 10, 5)
print(result)  # Output: 50



# Returning Lambda Function from a Function
def multiplier(n):
    return lambda x: x * n

times3 = multiplier(3)
print(times3(4))  

# IFFE
result = (lambda x, y: x + y)(5, 10)
print(result)  # Output: 15'

# local variable
def greet():
    message = "Hello"  # Local variable
    print(message)

greet()

# global

name = "Rahul"  # Global variable

def say_hello():
    print("Hello", name)

say_hello()


# global
count = 0

def increment():
    global count
    i = 0
    while(i< 10):
        count += i
        i = i + 1

increment()
print(count)  # Output: 45

x = 10

def show_globals():
    print(globals()['x'])  # Output: 10

show_globals()