# Static Method

class demo2:

    @staticmethod
    def m1():
        print("Method M1")

    @staticmethod
    def EmpName(Names):
        print("Employees Name:",Names)

    @staticmethod
    def math(N1,N2):
        print("Math calculation:", N1*N2)
        print("Math calculation:", N1+N2)
        print("Math calculation:", N1-N2)
        print("Math calculation:", N1/N2)


demo2.m1()

demo2.EmpName("Rushi")

demo2.math(5,5)

