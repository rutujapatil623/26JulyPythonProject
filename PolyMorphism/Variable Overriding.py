#Ex2 Print variable override from the child class

class Parent:

    Name = "rutuja"     # Parent class variable


class Child(Parent):
    Name = "RUTUJA"  # same variable from parent just changed data


c = Child()

print("Variable of child class:", c.Name)


#Ex Print variable from Parent & child class

class Fruits:

    Fruit = "Apple"

class Health(Fruits):

    Fruit = "APPLE"                            #Class variable

    def eat(self):
        print(super().Fruit)
        print(self.Fruit)    #need call with self object

h = Health()
h.eat()