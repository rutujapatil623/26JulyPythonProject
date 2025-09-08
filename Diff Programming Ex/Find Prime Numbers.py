
Num = 27

if Num > 1:
    for i in range(2,Num,1):
        if Num % i == 0:
            print("Number is not prime")
            break
    else:
            print("Number is prime")

else:
    print("Number is not prime")

