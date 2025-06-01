def calculate_product(numbers):
    product=1
    for num in numbers:
        product *=num
    return product
my_tuple=(59,65,68,65)
result=calculate_product(my_tuple)
print("product of all numbers in the tuple",result)