#Method we have to declare inside Class

#Non-Static Method

class demo1:

    def m1(self):
        print("Method M1")

    def m2(self,Num):
        print("The Number is:",Num)

    def math(self,Num1,Num2):
        print("The Cal:",Num1+Num2)

    def Name(self,Names):
        print("The names:",Names)

d = demo1()

d.m1()

d.m2(20)

d.math(20,10)

d.Name("Rutuja")




