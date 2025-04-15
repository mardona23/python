for i in range(1,5):
    for j in range(1,11):
        print(j, end=" ")
    print()
a=input("Enter your str")
b=input("enter your char")
i=0
count=0
while(i<len(a)):
    if a[i]==b: 
        count=count+1
    i=i+1
print(count)