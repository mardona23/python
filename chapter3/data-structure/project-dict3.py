my_dict={'name':'neymar','age':31,'hobby':'football'}
print(my_dict)
print(my_dict['age'])
print(my_dict['name'])
print(my_dict['hobby'])
print(my_dict['age'])
my_dict['age']=2945
print(my_dict)
my_dict['marks']=100
print(my_dict)
print(my_dict.pop('hobby'))
print(my_dict)
print(my_dict.get('name'))
for i in my_dict:
    print(i)