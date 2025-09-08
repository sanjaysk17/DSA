def recur(num):
    if(num==0):
        return
    else:
        print(num,end=" ")
        return recur(num-1)
n=int(input("Enter a number"))
recur(n)