mark=int(input("Enter your Mark: "))
if mark>=90:
    print("Grade A")
elif mark>=70:
    print("Grade B")
elif mark>=50:
    print("Grade C")
elif mark>=35:
    print("Grade D")
else:
    print("Fail")
     

 #Second Question
age=int(input("Enter a Age:"))
if age>=18:
    print("You are Elgible For VOting")
else:
    print("You are Not Eligble For Voting") 
    #
year=int(input("Enter a Year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Not a Leap Year")
else:
     print("Not a Leap Year")