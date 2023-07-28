class employee:
    def __init__(self):
        self.__name = "Jayesh"

a = employee()
# print(a.__name) Cannot be accessed direclty
print(a._employee__name) # can be accessed indirectly
print(a.__dir__())