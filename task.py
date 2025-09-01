#count the digits
n=int(input("Enter the number:"))
count=0
print(count)
while n!=0:
    n=n//10
    count+=1
print(f"Digits of the Number:{count}")
#Reverse the Number
num=int(input("Enter the Number to Reverse:"))
tem=num
rev=0
r=0
while tem!=0:
    r=tem%10
    rev=rev*10+r
    tem=tem//10
print(f"The reverse Of the Number is {rev}")