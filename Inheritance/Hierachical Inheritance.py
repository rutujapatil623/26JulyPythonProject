# Hierarchical Inheritance - Multiple sub classes can acquire properties of 1 superclass

class father:

    def money(self):
        print("Father Class - Method money")

    def home(self):
        print("Father Class - Method home")

    def car(self):
        print("Father Class - Method car")

class son1(father):

    def mobile(self):
        print("Son1 Class - Method mobile")

class son2(father):

    def laptop(self):
        print("Son2 Class - Method laptop")

s1 = son1()

s1.money()
s1.home()
s1.car()
s1.mobile()

print("-------------------------------------------------------")

s2 = son2()

s2.money()
s2.home()
s2.car()
s2.laptop()

