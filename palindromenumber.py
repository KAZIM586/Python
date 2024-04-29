n=int(input("Enter a number: "))
temp = n
reverse = 0
while(n>0):
    rem = n % 10
    reverse = reverse * 10 + rem
    n = n // 10
if(reverse == temp):
    print(f"{temp} is a palindrome number")

else:
    print(f"{temp} is not a palindrome number")
