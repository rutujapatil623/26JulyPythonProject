#position of parameters are matter

def studentdetails(RollNo,Name):
   print("RollNo of student", RollNo)
   print("Name of the student", Name)


studentdetails("Rutuja",101)   #Wrong Order
studentdetails(102,"Abhijeet")

print("----------------")

#Default Value to the parameters

def employeedetails(name,salary=80000):
    print("Employees Name:",name)
    print("Employees Salary:",salary)

employeedetails("Rutuja")
employeedetails("Ravi",30000)

print("------------")

#Parameter order will not matter if mention them as below

def cal(A=5,B=10):
    C=A*B
    D=A+B

    print(C , D)
    return C,D


cal(B=25, A=30)


M,N=cal(20,5)

M,N=cal(20)

M,N=cal()

print("Addition & Multiplication:",M,N)


