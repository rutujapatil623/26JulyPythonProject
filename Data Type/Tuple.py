Tp=("Abhi",101,"B+",85.10,101,"BE")

print(Tp)

#Tp[0]="ABHI"    # We cannot modify the tuple once it is declared

#print particulare index data

print(Tp[0])

#Check the type of object

print(type(Tp))

#Check the length of object

print(len(Tp))

#Adding element

Tp1 = Tp +("Mech",99)

print(Tp1)

Tp2 = Tp1 +(60,)

print(Tp2)

trup = (10,60,90,40,70)

#Sorting Tuple
Tp3 = tuple(sorted(trup))

print(Tp3)

#Reverse Sorting

revers_Tp3 = Tp3[::-1]

print(revers_Tp3)

#Print the data in the tuple

for i in Tp3:
    print(i)

print("------------------------------------")

for i in range(2,4):

    print(Tp3[i])

Tp3 = Tp3 + (60,90)

#Counting and indexing
#Check the index of particular data from list

print(Tp3.index(10))

#How many times the element are repeated in list

print(Tp3.count(60))
