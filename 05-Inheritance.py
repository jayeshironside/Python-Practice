class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the employee: {self.id} is {self.name}")

class programmer(employee):
    def showLanguages(self):
        print("The default language is python")

a = employee("Jayesh", 25)
a.showDetails()
b = programmer("Jay", 1)
b.showDetails()
b.showLanguages()