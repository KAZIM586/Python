n=int(input("Enter a 1number: "))
count  = len(str(n))
temp = n
sum = 0
while (n > 0):
    digit = n%10
    sum = sum + (digit ** count)
    n = n //10
if (sum == temp):
    print(f"{temp} is a armstrong number ")

else:
    print(f"{temp} is not a armstrong number ")
