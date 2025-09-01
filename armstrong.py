n=int(input("Enter a Number:"))
temp=n
forcheck=n
rev=0
count=0
while n!=0:
    n=n//10
    count+=1
while temp!=0:
    r=temp%10
    rev=rev+(r**count)
    temp=temp//10
if forcheck==rev:
    print("It is Armstrong Number")
else:
    print("It is not a Armstrong Number")
