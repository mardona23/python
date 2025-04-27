def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
print("please enter the choice")
print("a. addtion")
print("b. substraction")
print("c. multiple")
print("d. division")
choice=input("enter you are choice")
a=int(input("Enter any number"))
b=int(input("Enter any number"))
if choice=="a":
    print(a+b,add(a,b))
elif choice=="b":
    print(a-b,sub(a,b))
elif choice=="c":
    print(a*b,mul(a,b))
elif choice=="d":
    print(a/b,div(a,b))
else:
    print("please enter correct value")