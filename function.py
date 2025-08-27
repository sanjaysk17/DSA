#Function add

def add(a,b):
    return a+b
a=int(input("Enter the Number A:"))
b=int(input("Enter the Number B:"))
result=add(a,b)
print(result)
print()


#Even or odd
def evenodd(num):
    if num%2==0:
        print("Even")
    else:
        print("odd")
num=int(input("Enter the Number:"))
evenodd(num)
print()

#greet Function
def greet(name='Guest'):
    print(f"Hello,{name}")
greet()

#greet Function
'''def greet(name): #It will eRror because it has no Arguement
    print(f"Hello,{name}")
greet()'''
print()
#greet Function
def greet(name='Guest'):
    print(f"Hello,{name}")
name=input("Enter your name")
greet(name)