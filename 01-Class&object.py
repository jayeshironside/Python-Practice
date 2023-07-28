class person:
    name= "Jay"
    occupation = "Business analyst"
    salary = 2000
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c = person()

a.name = "Jayesh"
a.occupation = "Data Analyst"

b.name = "Akshay"
b.occupation = "QA"

a.info()
b.info()
c.info()