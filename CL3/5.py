#Create a dictionary to store name and marks of 10 students by user input
d={}
name=""
marks=""
for x in range(10):
	name=input("enter name of the student : ")
	marks=int(input("enter mark of the student : "))
	d[name]=marks
print("dictionary is : ")
print(d)
