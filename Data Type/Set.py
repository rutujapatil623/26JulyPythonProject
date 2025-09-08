#Creating a set

St = {10,20,"xyz",10,"abc"}

print(St)

#Length and Type

print(len(St))
print(type(St))

#Adding the elements

St.add(4)

print(St)

#Remove the element

St.remove(20)

print(St)

St.discard(10)

print(St)

removed_item = St.pop()

print(f"Removed Item:{removed_item}")
print("Removed Item:", removed_item)

print(St)

St.add(10)
St.add(60)

print(St)

#Sorting

St2={10,60,20,40}

Sorted_St = sorted(St2)

print(Sorted_St)

#We cant use index(), Count() in the set

print(60 in St)

St3 = St2.copy()

print(St3)

#Delete the set object

St3.clear()
print(St3)

del St3

# print(St3)      #Will get an error

Sttt={"abc",3,6,7}
del Sttt
# print(Sttt)

#print all the elements from set object

Stnew = {"puja",1,4}

for i in Stnew:
    print(i)
