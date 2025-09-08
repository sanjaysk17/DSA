def rec(num):
    if(num==0):
        return
    else:
        print(num,end=" ")
        return rec(num-1)
num=int(input("Enter a Number:"))
rec(num)