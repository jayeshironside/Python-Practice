class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = employee("Harry", 2000)
print(e.name)
print(e.salary)