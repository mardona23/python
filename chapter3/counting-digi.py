def count_digits(n):
    n=abs(n)
    count=0
    if n==0:
        return 1
    while n>0:
        n //=10
    count += 1
    return count
print(count_digits(12345))