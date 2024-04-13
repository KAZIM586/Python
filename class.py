# class DemoClass:
#     name=""
#     age=0
# demoobj = DemoClass()  #object creation of class
# demoobj.name="Monu"
# demoobj.age=39

# print(demoobj.name)
# print(demoobj.age)


# class Democlass:
#     a=10
#     b=90
#     def showvalue(self):
#         self.c= self.a+self.b
#         print(self.c)
# obj1=Democlass()
# obj1.showvalue()
# obj1.showvalue()
# obj1.showvalue()
# obj1.showvalue()

# print(obj1.a)
# print(obj1.b)
# print(obj1.a + obj1.b)
# obj2=Democlass()
# obj2.a=45
# obj2.b=98
# obj2.showvalue()

# obj3=Democlass()
# obj3.a=45
# obj3.b=45
# obj3.showvalue()
#  def showvalue(self):
#         self.c= self.a+self.b
#         print(self.c)

# class employee:
#     emp_code=0
#     emp_name=''
#     emp_designation=''
#     def showvalue(self):
#         print(self.emp_name)
#         print(self.emp_code)
#         print(self.emp_designation)


# obj1 =employee()
# obj1.emp_code=101
# obj1.emp_name='Monu'
# obj1.emp_designation='Java'
# obj1.showvalue()

# obj2 =employee()
# obj2.emp_code=102
# obj2.emp_name='sonu'
# obj2.emp_designation='JavaScript'
# obj2.showvalue()

# obj3 =employee()
# obj3.emp_code=103
# obj3.emp_name='Mohit'
# obj3.emp_designation='C++'
# obj3.showvalue()

# obj4 =employee()
# obj4.emp_code=104
# obj4.emp_name='Monu'
# obj4.emp_designation='Java'
# obj4.showvalue()

# obj5 =employee()
# obj5.emp_code=105
# obj5.emp_name='Mohan'
# obj5.emp_designation='C'
# obj5.showvalue()

# print(obj1.emp_code)
# print(obj1.emp_name)
# print(obj1.emp_designation)



# class employee:
#     def printInfo(self,emp_code,emp_name,emp_designation):
#         self.emp_code=emp_code
#         self.emp_name=emp_name
#         self.emp_designation=emp_designation
#         print("Employee code is = ",self.emp_code)
#         print("Employee name is = ",self.emp_name)
#         print("Employee designation is = ",self.emp_designation)
# emp1=employee()
# emp1.printInfo(101,'Raju',"Java Trainer")
# emp1.printInfo(102,'Mahesh',"Python Trainer")



class student():
    def printInfo(self,st_id,st_name,st_course,st_fee):
        self.st_id=st_id
        self.st_name=st_name
        self.st_course=st_course
        self.st_fee=st_fee
        print("Student id is = ",self.st_id)
        print("Student name is = ",self.st_name)
        print("Student course is = ",self.st_course)
        print("Student fee is = ",self.st_fee)
stu1=student()
stu1.printInfo(101,"Kazim","FullStack developer",56000)
stu2=student()
stu2.printInfo(102,"Neetan","C++",65000)
stu3=student()
stu3.printInfo(103,"Himanshu","Java",60000)
stu4=student()
stu4.printInfo(104,"Gaurav","Python",90000)
stu5=student()
stu5.printInfo(105,"Atul","C++",80000)


