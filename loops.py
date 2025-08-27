#for loop
for i in range(1,10,2):
    print(i)
print()
for i in range(10,1,-2):
    print(i)
print()
str="SANJYAKUMAR S"
for i in str:
    print(i)
i=0

print()
#While Loop


while i<=5:
    print(i)
    i=i+1
print()
#Break Statement

for i in range(20):
    if i==7:
        break
    else:
        print(i)

print()
#Continue
for i in range(10):
    if i%2==0:
        continue
    print(i)
         
print()
#pass
for i in range(15):
    if i%2==0:
        print(i)
        pass
    print(i)
print()
#Nested Loop   
for i in range(3):
    for j in range(2):
        print(f"i={i} and j={j}")
