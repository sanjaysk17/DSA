def Prime(n):
    if n==2:
        return "prime"
    else:
        for i in range(2,(n//2)+1):
            if(n%i==0):
                return "Not Prime"
        return "prime"
num=int(input("Enter a Number to Check for a Prime"))
prime=Prime(num)
print(prime)