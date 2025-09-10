#Ex3 Method Overriding with super() keyword
# Use: Add New Functionality into existing functionality

class A:
    def m1(self):
        print("Method m1 is part of parent class")

class B(A):
    def m1(self):
        super().m1()
        print("Method m2 is part of child class")

a = B()
a.m1()