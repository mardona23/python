try:
    age=int(input("Enter your age:"))
    if(age<18):
        raise ValueError
    else:
        print("The age is valid")
except ValueError:
    print("The age is not valid")
    if age%2==0:
        print("age is even")
else:
    print("age is odd")