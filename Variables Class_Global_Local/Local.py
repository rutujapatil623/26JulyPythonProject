#Local - A Variable declared inside a function or method is called a local variable.
#Accessible with in the function or block we declared.

class demo4:

    def m5(self):
        Name= "Rutuja"
        print("Print the Name:", Name)


    @staticmethod
    def m6(gender):
        print("print qqwwwwwwwwwwwwwwwwwwwwwww gender:", gender)


d2 = demo4()

d2.m5()

demo4.m6("Female")





