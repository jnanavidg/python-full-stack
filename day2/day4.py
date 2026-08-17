#class student:
 #   def display(self):
  #      print("Hello students")
#s1=student()
#s1.display()

# class student():
#     def __init__(self,name,age,course):
#         self.name=name
#         self.age=age
#         self.course=course
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Course:",self.course)
# s1=student("John",20,"Computer Science")
# s1.display()

# class employee():
#     def __init__(self,name,age,department):
#         self.name=name
#         self.age=age
#         self.department=department
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Department:",self.department)
# e1=employee("Alice",30,"HR")
# e1.display()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# class Employee(Person):
#     def __init__(self, name, age, department, salary):
#         super().__init__(name, age)  
#         self.department = department
#         self.salary = salary
    
#     def display(self):
#         super().display()
#         print("Department:", self.department)
#         print("Salary:", self.salary)

# class Manager(Employee):
#     def __init__(self, name, age, department, salary, team_size):
#         super().__init__(name, age, department, salary)
#         self.team_size = team_size
    
#     def display(self):
#         super().display()
#         print("Team Size:", self.team_size)

# m1 = Manager("Bob", 40, "IT", 80000, 10)
# m1.display()

# e1 = Employee("Alice", 30, "HR", 50000)
# e1.display()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# # Level 2: Parent Class - inherits from Person
# class Employee(Person):
#     def __init__(self, name, age, department, salary):
#         super().__init__(name, age)  
#         self.department = department
#         self.salary = salary
    
#     def display(self):
#         super().display()
#         print("Department:", self.department)
#         print("Salary:", self.salary)

# # Level 3: Child Class - inherits from Employee
# class Manager(Employee):
#     def __init__(self, name, age, department, salary, team_size):
#         super().__init__(name, age, department, salary)
#         self.team_size = team_size
    
#     def display(self):
#         super().display()
#         print("Team Size:", self.team_size)

# # Creating object of Manager (inherits from all 3 levels)
# m1 = Manager("Bob", 40, "IT", 80000, 10)
# m1.display()

# class car:
#     def move(self):
#         print("Car is moving")
# class bike:
#     def move(self):
#         print("Bike is sailing")
# class plane:
#     def move(self):
#         print("Plane is flying")
# vehicles=[car(),bike(),plane()]
# for vehicle in vehicles:
#     vehicle.move()



class BankAccount:
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder  
        self.__balance = balance                 
    
    
    def get_account_holder(self):
        return self.__account_holder
    
    # Getter for balance
    def get_balance(self):
        return self.__balance
    
    # Setter for balance with validation
    def set_balance(self, amount):
        if amount < 0:
            print("Error: Balance cannot be negative!")
        else:
            self.__balance = amount
    
    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive!")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Error: Insufficient balance!")
        elif amount > 0:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}. New Balance: ${self.__balance}")
        else:
            print("Error: Withdrawal amount must be positive!")
    
    def display(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: ${self.__balance}")

# Creating object and using encapsulation
account = BankAccount("John Doe", 1000)
account.display()
print()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # This will fail
print()
account.display()





    
    
  