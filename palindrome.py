num=int(input("Enter the Number to Reverse:"))
tem=num
rev=0
r=0
while tem!=0:
    r=tem%10
    rev=rev*10+r
    tem=tem//10
print(f"The reverse Of the Number is {rev}")
if rev==tem:
    print("It is palindrome")
else:
    print("Not a palindrome")