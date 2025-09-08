# Local, Global, and Class variable

#Global-Declare outside a class or function called Global. Throughout the Python file, we can access.

Num = 10

class demo3:

    def m1(self):
        print("Print the Global Variable:",Num)

    @staticmethod
    def m2(N):
        print(Num+N)



d1 = demo3()

d1.m1()

d1.m2(10)

