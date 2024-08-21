
import mymodule

print( ' ')

#todo Day 8 #1 , #2

dog = {
    'name': 'Barsik',
    'color': 'Black',
    'breed': 'Best_home',
    'legs': 4,
    'age': 16
}
#print(dog)

#todo #3, #4, #5
student = {
    'first_name': 'Anton',
    'last_name': 'BEgemot',
    'gender': 'Male',
    'age': '33',
    'marital status': 'single',
    'skills': ['SQL', 'HTML', 'CSS', 'Python', 'Testing'],
    'country': 'Ukraine',
    'city': 'Kharkiv',
    'address': {
        'street': 'Plehanovska, 43',
        'zip_code': 11100
    }
}

#skill_values = student['skills']
#print(type(skill_values), '\nskills: ', skill_values)
#print(student['address']['street'])

student['skills'].append('Charles')
student['skills'].append('GraphQL')
#print(student['skills'])

# my_dict = {
#     'fruits': ['apple', 'banana'],
#     'vegetables': ['carrot', 'broccoli']
# }
#
# new_vegetable = 'spinach'
# if 'vegetables' in my_dict:
#     my_dict['vegetables'].append(new_vegetable)
# else:
#     my_dict['vegetables'] = [new_vegetable]
#print(my_dict)

#todo #7-8

# print(student.keys())
# print(student.values())
# print(student.items())

#todo #9
student.pop('age')
#print(student)

#==============================================================
print(mymodule.info_user('Anton', 'Kolomiiets'))



