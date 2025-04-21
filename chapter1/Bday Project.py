birthdays={}
for i in range(5):
    name=input("Enter the name of friend #{i+1}:")
    birthday=input("enter{name}´s birthday")
    birthdays[name]=birthday
print("friend's birthday:")
for name, birthday in birthdays.items():
    print("{name}: {birthday}")    