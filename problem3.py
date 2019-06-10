#!usr/bin/python
l=input("enter the numbers")
list=l.split()
a=[]
b=[]
for i in list:
	if int(i)>5 :
	 a.append(i)
	elif int(i)<=2 :
	 b.append(i)
print("The no. greater than 5 are :")
for j in a :
	 print(j)
print("The no. less than or equal to 2 are :")
for j in b :
	 print(j)
	  

	

