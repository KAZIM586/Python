# class student:
#     age=0
#     name=""
#     def __init__(self):
#         self.age=25
#         self.name="mohit"

#     def show(self):
#         print(self.age)
#         print(self.name)

# st=student()
# st.show()


# class student:
#     def __init__(self,age,name,city):
#         self.age=age
#         self.name=name
#         self.city=city
#         print(self.age)
#         print(self.name)
#         print(self.city)

    # def show(self):
    #     print(self.age)
    #     print(self.name)
    #     print(self.city)

# st=student(45,'mohan','delhi')
# st2=student(25,'Gopu','chhattarpur')
# st3=student(45,'Neetan','delhi')
# st.show()




class vehicle:
    def __init__(self,v_no,v_type,v_name):
        self.v_no=v_no
        self.v_type=v_type
        self.v_name=v_name
        print(self.v_no)
        print(self.v_type)
        print(self.v_name)
vi=vehicle('DL-4578','petrol','Audi')
vi2=vehicle('DL-9578','petrol','Honda city')
vi3=vehicle('MP-8878','diesel','Maruti suzuki')
vi4=vehicle('UP-1111','diesel','Alto')
