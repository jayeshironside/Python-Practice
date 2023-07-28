class person:
    def __init__(self, name, ooccupation):
        print("Hey my name is JAY")
        self.name = name
        self.occupation = ooccupation
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person("Jayesh", "Business analyst")
b = person("Jaykumar", "Data Analyst")
c = person(1, 2)

a.info()
b.info()
c.info()