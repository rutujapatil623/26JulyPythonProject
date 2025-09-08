def mathoperations(Num1,Num2):
    Ans1=Num1*Num2
    Ans2=Num1+Num2
    Ans3=Num1-Num2
    Ans4=Num1/Num2
    return Ans1,Ans2,Ans3,Ans4

#A1=mathoperations(20,10)

A1,A2,A3,A4=mathoperations(20,10)

print(A1,A2,A3,A4)

print(type(A1))

for i in A1:
    print(i)

print("Result of math operations:", A1)

print("----------")

def employeesalary():
    FN="Rutuja"
    LN="Patil"
    Salary=80000
    Qualification="BE"
    return FN,LN,Salary,Qualification

First,Last,Sal,Qual =employeesalary()

print("Employee details:",First,Last,Sal,Qual)


print("------------")

def multiplication(A,B,E,F):
    C=A*B
    D=E*F

    print("Inside Function Result:",D)
    return C,D

M,N= multiplication(10,5,8,4)

print("Multiplication Result:", M,N)






