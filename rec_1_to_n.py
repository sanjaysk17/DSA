def rec(n,i):
    if(i==n):
        return
    else:
        print(i,end=" ")
        return rec(num,i+1)
num=int(input("Enter a Number:"))
i=1
rec(num+1,i)