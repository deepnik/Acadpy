
#     add in previous list     ["Google","Apple","Facebook","Microsoft","Tesla"]   


l=[]

num1= int(input("Enter first number= "))
num2= int(input("Enter second number= "))
num3= int(input("Enter third  number= "))
l.append(num1)
l.append(num2)
l.append(num3)
print("List created: then    l = ",l)


#adding new list by using extend function

l2=["Google","Apple","Facebook","Microsoft","Tesla"]
l.extend(l2)
print("After added both lists :  Then     l= ",l)
