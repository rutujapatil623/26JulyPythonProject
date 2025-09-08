# It is an operation where inheritance takes place between only 2 classes
# To perform single level inheritance only 2 classes are mandatory

class father:

    def Money(self):
        print("method Money is part of father class")

    def Home(self):
        print("method Home is part of father class")

    def Car(self):
        print("method Car is part of father class")

class son(father):                          # Son inheritance all data of father class

    def Mobile(self):
        print("method Mobile is part of son class")


s = son()      # Son class object created -> it will copy members(method, variable) of class into object

s.Money()
s.Home()
s.Car()
s.Mobile()
