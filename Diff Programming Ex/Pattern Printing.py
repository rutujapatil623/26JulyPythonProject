#block of * (like a solid rectangle),

for i in range(1,5,1):
    for j in range(1,6,1):
       print("*",end= " ")
    print()

print("-----------------------------------------------")

#hollow rectangle (block with empty space inside).

for i in range(1,5,1):
    for j in range(1,6,1):
        if i == 1 or i == 4 or j == 1 or j==5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("-------------------------------------------------")

for i in range(1,6,1):
    for j in range (1,i,1):
        print("*",end=" ")
    print()

print("-------------------------------------------------")

for i in range(5,1,-1):
    for j in range(1,i,1):
        print("*",end=" ")
    print()

print("--------------------------------------------------")

n=6

for i in range(1,n,1):
    for j in range(1,n-i,1):
        print(" ",end=" ")
    for j in range (1,i,1):
        print("*",end=" ")
    print()


