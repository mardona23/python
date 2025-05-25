x1=[5,10,20,35,55,77,99]
x2=["messi","ronaldo","nani","yamal"]
print(len(x1))
print(len(x2))
print(x1[0])
print(x2[3])
print(x2[-3])
print(x1[3:6])
for i in x2:
    print(i)
x3=x1+x2
print(x3)
print(max(x1))
print(min(x1))
x2.append(19)
print(x2)
x4=[30,59,88,]*7
print(x4)