#Basic example same function but different behaviour

print(5+5)       #10

print("5"+"5")   #55

print("-------------------------------")

s1 = "abcd"
print(len(s1))    #Total no of char = 4

l1 = {"abc",10,20.5}   #Total no of element = 3
print(len(l1))

#Ex1: How Method Overriding works

class Grandfather:

    def Home(self):
        print("1 BHK")

    def Money(self):
        print("1 lakh")

class Father(Grandfather):        #Method Overriding

    def Home(self):
        print("2 BHK")

    def Money(self):
        print("2 lakh")

class Son(Father):
    def Home(self):
        print("3 BHK")

    def Money(self):
        print("3 lakha")

print("------------Properties of Grandfather-----------")

g = Grandfather()
g.Home()
g.Money()

print("------------Properties of Father----------------")

f = Father()
f.Home()
f.Money()

print("------------Properties of Son----------------")

s = Son()
s.Home()
s.Money()