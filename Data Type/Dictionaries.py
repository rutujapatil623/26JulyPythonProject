dict = {1:10,2:"Rutuja",3:10.5,4:"Xyz",5:20}

print(dict)

#Check the Length and Type

print(len(dict))

dict1 = {1:"Rutuja",2:"puja",3:"Abhi",4:"Rushi"}

print(type(dict1))

dict2 = {1:"abhu","dabu":60,4:"Subhu"}

print(dict2)

#Get Values of specific key

print(dict2["dabu"])

print(dict1[1])

#Add new K-V pair
dict1[5]="Rushi"

print(dict1)

#Modify/Update k-V pair

dict1[1]="RUTUJA"

dict1[2]="Usha"

print(dict1)

#Remove K-V

dict2.pop(1)

print(dict2)

#Remove last inserted item(K-V)

dict2.popitem()

print(dict2)

#Check the key exist in object

print(1 in dict1)

print(6 in dict2)

#print all the values from object

for i in dict1:
    print(i)             #it's only returning the keys

#Print All Keys

#K = dict1.keys
#print(K)

print(dict1.keys())

#Print Values

print(dict1.values())

#Print All Keys-Values

print(dict1.items())

#Print All Keys-Values

print(dict1.keys(),dict1.values())

#Print Keys and Values using for loop

for key,value in dict1.items():
    print(key,value)

#Print Keys using for loop

for key in dict1.keys():
    print(key)

#Print Values using for loop

for value in dict1.values():
    print(value)
