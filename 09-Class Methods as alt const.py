class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e = employee("Harry", 12000)
print(e.name)
print(e.salary)