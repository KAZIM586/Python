# hiding not necessary detail
from abc import ABC,abstractmethod

class test(ABC):
  @abstractmethod
  def show(self):
   pass

class test1(test):
       def show(self):
        print("Hi  i am showing the data of test 1" )
        print("Hamara object create karo tabhi output doonga" )
        print("parent class ka object bna ke output lena chahoge to error dunga")
class test2(test):
       def show(self):
        print("Hi  i am showing the data of test 2 " )
        print("Hamara object create karo tabhi output doonga tumhe" )
t1=test1()
t1.show()
t2=test2()
t2.show()