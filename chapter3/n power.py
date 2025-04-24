base=float(input("Enter the base number "))
n=int(input("Enter how many number to calculate "))
print(f"\npowers of {base} up to {n}:")
for i in range(1,n+1):
    result=base**i
    print(f"{base}^{i}={result}")