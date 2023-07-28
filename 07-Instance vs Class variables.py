class employee:
    companyName = "Facebook" #Classs variable
    NoOfEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 20
        employee.NoOfEmployees +=1
    
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} sied of {self.NoOfEmployees} employees is {self.raise_amount}")

emp1 = employee("Jayesh")
emp1.showDetails()
emp2 = employee("jaykumar")
emp2.companyName = "Google" #Instance variable
emp2.raise_amount = 30
emp2.showDetails()