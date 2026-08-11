 a = int(input("Enter a number: "))
 b = int(input("Enter another number: "))
 print(a+b)

 a =float(input("Enter a number: "))
 b = float(input("Enter another number: "))
 print(a+b)
 print(a-b)
 print(a*b)
 print(a/b) 

 num = int(input("Enter a number: "))
 print(num % 2 == 0)

age = 30
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")   
elif num < 0:
    print("The number is negative.")
elif num == 0:
    print("The number is zero.")

correct_pin="1234"
pin = input("Enter your pin: ")
if pin == correct_pin: 
    print("Access granted.")
    print("Welcome to the system!")
else:
    print("Access denied.")
    print("Incorrect pin. Please try again.")

for i in range(0,10):
    print("Welcome to the RIT")
for i in range(3):
    for j in range(5):
        print("*", end="")
    print()
 
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
