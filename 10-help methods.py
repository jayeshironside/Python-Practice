x = [1, 2, 3]
print(dir(x)) #dir method returns the list of all the attributes and methods.



class person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

p = person("Jayesh", 20)
print(p.__dict__) # __dict__ will create a dictionary of all the attributes of the class

print(help(person)) # help function is used to get help documentation for the object including the description of the attributes and its methods
