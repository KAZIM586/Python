# class Student:
#     def __init__(self):
#      self.__marks=0
#     def getMarks(self):
#        return self.__marks
#     def setMarks(self,marks):
#        self.__marks=marks
# st=Student()
# st.setMarks(55)
# print(st.getMarks())


class Teacher:
    def __init__(self):
     self.__teacher_id=0
     self.__teacher_name=0
     self.__teacher_age=0
     self.__teacher_exp=0
    def getData(self):
       return self.__teacher_id,self.__teacher_name,self.__teacher_age,self.__teacher_exp
    def setData(self,teacher_id,teacher_name,teacher_age,teacher_exp):
       self.__teacher_id=teacher_id
       self.__teacher_name=teacher_name
       self.__teacher_age=teacher_age
       self.__teacher_exp=teacher_exp
st=Teacher()
st.setData(101,"Nidhi Arora",35,"10 Years")
print(st.getData())




