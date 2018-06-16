# two one dimensional arrays A & B which are sorted in ascending order .
#  Write a program to merge them in a single sorted array C that in ascending order(list).


print("First list craetion.....")
A=[]

num1= int(input("Enter first number= "))
num2= int(input("Enter second number= "))
num3= int(input("Enter third  number= "))
num4= int(input("Enter fourth  number= "))
num5= int(input("Enter fifth  number= "))
A.append(num1)
A.append(num2)
A.append(num3)
A.append(num4)
A.append(num5)
print(" Ist List created:     A = ",A)

print(A.sort())
print("\n")
print("List 'A' after sorting= ",A)

print("\n\n\n\n")
print("Second list creation.....")
B=[]

num1= int(input("Enter first number= "))
num2= int(input("Enter second number= "))
num3= int(input("Enter third  number= "))
num4= int(input("Enter fourth  number= "))
num5= int(input("Enter fifth  number= "))
B.append(num1)
B.append(num2)
B.append(num3)
B.append(num4)
B.append(num5)
print("Second List created:     B = ",B)

print(B.sort())
print("\n")
print("List 'B' after sorting= ",B)

print("\n\n\n\n")

print("List 'C' formed after adding A & B list..." )
C=[]
print(C.extend(A),C.extend(B))
print("List C= ",C)
print(C.sort())
print("\n")
print("List 'C' after sorting= ",C)


