#Ex 1 Constructor with Parameters

class testing:

    num = 100     #Class Variable

    def __init__(self, name):   #Constructor with parameters,name is an local variable
       print("Constructor with Para:", name)
       self.name = name        #to use constructor parameter in all over the class we have to convert local variable into class

       print("Number:", self.num)

    def m1(self,edu):
        print("Print name & edu:", self.name, edu)

        print("Number:", self.num)


test = testing("Rutuja")

test.m1("BE")

#Ex 2

class employee:

    def __init__(self, names,ids,salary):
        self.name = names
        self.id = ids
        self.salary = salary

    def math(self):
        print("Name,ID and salary of Employee:",self.name,self.id,self.salary)

e = employee("Ruruja",101,80000)

e.math()

e = employee("Abhi",102,70000)

e.math()

#Ex 3

class mathOperations:

    def __init__(self, Num1, Num2):
        self.No1 = Num1
        self.No2 = Num2

    def addition(self):
        print(self.No1 + self.No2)

    def Multiplication(self):
        print(self.No1 * self. No2)

    def Substraction(self):
        print(self.No1 - self.No2)


math = mathOperations(10,15)

math.addition()
math.Multiplication()
math.Substraction()

math = mathOperations(20,25)

math.addition()
math.Multiplication()
math.Substraction()


