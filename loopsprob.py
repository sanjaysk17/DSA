#Factorial
num=int(input("Enter the Number For FActorial:"))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print(f"The factorial of the Number is {fact}")
print()
#sum of Natural Numbers
num=int(input("Enter the Number"))
sum=0
for i in range(num):
    sum=sum+i
print(f"The sum of {num} number is {sum}")