try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")

# This code cannot be terminated
# by pressing Ctrl-C.
 
# from time import sleep
 
# seconds = 0
 
# while True:
#     try:
#         print(seconds)
#         seconds += 1
#         sleep(1)
#     except KeyboardInterrupt:
#         print("Don't do that!")


# more general exception is listed first 
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")
 
print("THE END.")

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

# exception is raised inside a function
def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")

# outside the function
def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

# rasie is a keyword. The ZeroDivisionError is raised twice:
def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")

import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)