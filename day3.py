names = ["nibba", "alex", "maria"]

def student():
    for name in names:
        print(name)

student()

for name in names:
    print(name)  # global scope

######local scope#####
def student():
    age = 20
    print(age)

student()

#local and global scope
age = 30   
print(age)  # global scope
def student():
    age = 20  # local scope
    print(age)
student()

name = "dev"
def display():
    name = "devi"
    print(name)
display()
print(name)

name = "dev"
name = "nanna"
def display():
    name = "devi"
    name = "nanni"
    print(name)
display()
print(name)

######################################
num=int(input("Enter a number: "))
def square(num):
    return num*num
result = square(num)
print("The square of", num, "is", result)

square = lambda x: x*x
print(square(3))

cube = lambda x: x*x*x
print(cube(3))

add=lambda x,y: x+y
print(add(3,5))

subtract=lambda x,y: x-y
print(subtract(10,5))

multiply=lambda x,y: x*y
print(multiply(3,5))

largest = lambda a,b: a if a>b else b
print(largest(10,20))

def countdown(n):
    if n == 0:
        print("Countdown finished!")
    else:
        print(n)
        countdown(n - 1)
countdown(5)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(4))

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
print(power(12, 16)) 





