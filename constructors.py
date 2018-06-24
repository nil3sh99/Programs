#default constructor

class defConstr:
    num =121

    def read_data(self,data):
        self.num = data
        print(self.num)

obj = defConstr()

obj.read_data(122)











# parametrized constructor

# class constructor:
#     num = 123

#     def __init__(self, data): #it is a default constructor which by default called when an object is created
#         self.num = data

#     def read_data(self):
#         print(self.num)

# obj = constructor(55)

# obj.read_data()

