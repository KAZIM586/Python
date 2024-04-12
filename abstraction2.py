from abc import ABC,abstractmethod

class car(ABC):
  @abstractmethod
  def milaege(self):
   pass

class suzuki(car):
       def milaege(self):
        print("I am giving 20kmph" )

class BMW(car):
       def milaege(self):
        print("I am giving 10kmph" )

class volvo(car):
       def milaege(self):
        print("I am giving 40kmph" )
s=suzuki()
b=BMW()
v=volvo()
s.milaege()
b.milaege()
v.milaege()