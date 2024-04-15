# lambda without argument
result=lambda:print("Hello world!!")
#calling
# result()

# lambda with argument
result1= lambda name:print("My name is ",name)
# result1('sonu')
# result1('Gaurav')

result2= lambda num1,num2:print(f"The sum of {num1} and {num2} is: ",(num1+num2))
# result2(4,5)
# result2(2,5)
# result2(3,5)
# result2(7,5)
# result2(8,5)

result3= lambda sq :print(f"The square of {sq} is:" ,sq*sq)
# result3(5)


