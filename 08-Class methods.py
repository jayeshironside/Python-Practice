class employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod #decorator ro use company name in class variable
    def changecompany(claas, newcompany):
        claas.company = newcompany

e1 = employee()
e1.name = "Jayesh"
e1.show()
e1.changecompany("Tesla")
e1.show()