# super keyword is used to call the parent class from child class

class parentclass:
    def parent_method(self):
        print("This is the parent method")

class childclass(parentclass):
    def parent_method(self):
        print("Jayesh")
        super().parent_method()
    def child_method(self):
        print("This is the child method")
        super().parent_method()

child_object = childclass()
child_object.child_method()
child_object.parent_method()

print("****************example-2******************")

class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class programmer(employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

rohan = employee("Akshay", "420")
harry = programmer("Jayesh", "123", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)