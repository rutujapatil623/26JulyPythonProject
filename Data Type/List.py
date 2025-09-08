ls = ["Rutuja","BE","Electronics",75.10,12623]

#Check Data in list variable
print(ls)

#Check Type of varibale

print(type(ls))

#Check Length of List Varibale

print(len(ls))

#Print Particular index data from the list

print(ls[0])

#Add/insert Data in list varibale (It will add data at end)

ls.append("Manual tester")
print(ls)

#Insert data at particular position

ls.insert(1,"Patil")

#Insert multiple data at end of list

ls.extend(["Tosca","Python Testing",5.10])
print(ls)

#Remove Data from the end of list

ls.pop()

#Remove data from particular index

ls.pop(2)

#Remove data from particular index with any index (If we dont know the index no)

ls.remove(75.10)

#Copy all the data from one list varibale to another

ls2=ls.copy()     #ls is another list varibale

#Print Data from the list variable

for i in ls:
    print(i)

#Print data from particulare range

for i in range(0,4):
    print(ls[i])

#Perform sorting (Asc/Desc)
#It will sort data if the list contain same type of Data

EmpNames = ["Rutuja","Vikas","Karishma","Rithu","Abhi"]

EmpNames.sort()  #only sort in asc
print(ls)

#Perform Desc (1st have to perform sorting then only we can perform descending)

EmpNames.reverse()
print(ls)

#Check the index of particulars data from list

print(ls.index("Rutuja"))

#How many times the element are repeated in list

No =[1,2,10,5,3,9,2,10,8,7,6,5,9]

print(No.count(2))

#Clear all the data from the list variable (List will remain)

EmpNames.clear()
print(EmpNames)

#Remove entire list

del EmpNames

#print(EmpNames)

#Modify data of particulare index

print(ls)

ls[0]="RUTUJA"
ls[1]="Kadam"

print(ls)









