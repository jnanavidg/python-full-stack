class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def hike(self, percentage):
        amount = self.salary * percentage / 100
        self.salary += amount
        return amount

    def display(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print()


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, id, name, salary):
        self.employees.append(Employee(id, name, salary))

    def show_employees(self):
        for emp in self.employees:
            emp.display()

    def hike_employee(self, id, percentage):
        for emp in self.employees:
            if emp.id == id:
                amount = emp.hike(percentage)
                print(emp.name, "got a hike of", amount)
                return

        print("Employee not found")

    def hike_all(self, percentage):
        for emp in self.employees:
            amount = emp.hike(percentage)
            print(emp.name, "got a hike of", amount)


manager = EmployeeManager()

manager.add_employee(1, "Alice", 50000)
manager.add_employee(2, "Bob", 60000)
manager.add_employee(3, "Charlie", 55000)

print("Before Hike:")
manager.show_employees()

print("Alice gets 10% hike:")
manager.hike_employee(1, 10)

print("All employees get 5% hike:")
manager.hike_all(5)

print("After Hike:")
manager.show_employees()