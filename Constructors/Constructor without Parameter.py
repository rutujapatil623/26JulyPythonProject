#Define Constructor (Constructor are special method which called/define __init__)
#Without Parameter/Zero Parameter
#Use: Initalize the Object -> Copy all members of class into object

class test1:

    def __init__(self):
        print("Will not right code in th constructor we use it for initialization ")

    def meth(self):
        print("Will write code in it")

t = test1()    #Constructor will get called, it will copy all members class into object

t.meth()


