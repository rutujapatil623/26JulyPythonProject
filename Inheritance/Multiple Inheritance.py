# 1 subclass acquiring properties of 2 superclass at the same times is known as multiple inheritance

class mother:

    def __init__(self):
        print("The constructor")

    def Home(self):
        print("Mother has ownership of house")

class father:

    def Car(self):
        print("Father has ownership of car")

class son(mother,father):

    def inherit(self):
        print("Has mother & father Property")

s = son()

s.Home()
s.Car()
s.inherit()

