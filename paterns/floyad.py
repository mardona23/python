a=int(input("Enter a row number"))
n=1
for i in range(1,a+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()