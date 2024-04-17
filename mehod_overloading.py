# method overloading

# class VIP:
#     def vsp(self, x=None,y=None):
#         f=1
#         if x==None and y==None:
#             print("Hello this is a example of polymrphism")
#             print("Thanks to visit")
#         elif x!=None and y==None:
#             for i  in range(1,x+1,1):
#                 f=f*i
#             print(f)
#         else:
#             print("Addition is:",x+y)
# obj=VIP()
# obj.vsp()
# obj.vsp(5)
# obj.vsp(3,4)



#Method overriding

# class Gopu:
#      def gopuDone(self):
#           print("Kaam kar liya hoo.")
# class Gopu2(Gopu):
#      def gopuDone(self):
#           print("Kaam kar liya hoo dobaraa karo.")    
#      def kyo(self):
#           print("Parctise ho jayegi .") 
# g=Gopu2()   
# g.gopuDone()
# g.kyo()


# class A:
#     x=0
#     def xyz(self, x):
#         self.x=x
#     def __add__(self, obj):
#         return self.x+obj.x
# o1=A()
# o1.xyz(40)
# o2=A()
# o2.xyz(30)
# print(o1+o2)



# class A:
#     x=0
#     def __init__(self, x):
#         self.x=x
#     def __add__(self, obj):
#         return self.x+obj.x
# o1=A(40)
# o2=A(30)
# print(o1+o2)


# class circle:
#     def area(self,radius):
#         self.radius=radius
#         return 3.14*(radius*radius)
    
# class rectangle(circle):
#     def area(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#         return length*breadth

# c=circle()
# print("The area of circle is",c.area(5))      
# r=rectangle()
# print("The area of rectangle is",r.area(5,7))


class circle:
    radius=4
    def area(self):
        print(3.14*self.radius*self.radius)
    
class rectangle(circle):
    len=4
    br=5
    def area(self):
      super().area()
      print(self.len*self.br)
      
r=rectangle()
r.area()