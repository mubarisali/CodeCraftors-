class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def get_details(self):
        return f"{super().get_details()}, Team: {self.team}"


class Developer(Employee):
    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def get_details(self):
        return f"{super().get_details()}, Tech Stack: {self.tech_stack}"


# Example Usage
manager = Manager("John", 10000, ["Alice", "Bob", "Charlie"])
print(manager.get_details())

developer = Developer("Alice", 8000, ["Python", "Java", "C++"])
print(developer.get_details())
