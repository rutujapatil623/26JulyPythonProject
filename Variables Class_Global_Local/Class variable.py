# Class- A variable declared inside a class, but outside a method, is called a class variable.
# Scope of this variable within the class, so the method declared inside can access the class variable.
# We access a class variable inside a method: classname.class
# We cannot call a class variable inside a Static method.

class demo5:

    Number = 10


    def m1(self):
        print("print the num:",self.Number)


    def math(self,Num):
        print("sum of two num:", Num+ self.Number)

d5 = demo5()

d5.m1()

d5.math(10)