#Create a class Cop. Initialize its name, age , work experience and designation.\
#  Define methods to add, display and update the following details.\
#  Create another class Mission which extends the class Cop.\
#  Define method add_mission _details. Select an object of Cop and access methods\
#  of base class to get information for a particular cop and make it available for mission.
class cop:
    def add(self,name,age,work_exp,designation):
        self.name=name
        self.age=age
        self.work_exp=work_exp
        self.designaation=designation
    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("work experience : ",self.work_exp)
        print("designation : ",self.designaation,"\n")
    def update(self,name,age,work_exp,designation):
        self.name = name
        self.age = age
        self.work_exp = work_exp
        self.designaation = designation

class mission(cop):
    def add_mission_details(self,mission):
        self.mission=mission
        print(self.mission)
        
name=input("Name:")
age=int(input("Age:"))
work_exp=input("Work Experience:")
designation=input("Designation:")

name1=input("Name1:")
age1=int(input("Age1:"))
work_exp1=input("Work Experience1:")
designation1=input("Designation1:")

m1= mission()
m1.add_mission_details("assigned")
m1.add(name,age,work_exp,designation)
m1.display()
m1.update(name1,age1,work_exp1,designation1)
m1.display()
