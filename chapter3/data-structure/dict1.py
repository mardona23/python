my_dict={'name':'adam','age':11,'gernder':'male'}
print(my_dict)
print(my_dict['age'])
print(my_dict['name'])
my_dict['age']=359
print(my_dict)
my_dict['marks']=23
print(my_dict)
print(my_dict.pop('gernder'))
print(my_dict)
print(my_dict.get('name'))
for i in my_dict:
    print(i)
