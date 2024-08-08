
print( ' ')

#todo Day 8 #1 , #2

dog = {
    'name': 'Barsik',
    'color': 'Black',
    'breed': 'Best_home',
    'legs': 4,
    'age': 16
}
print(dog)

#todo #3, #4
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

skill_values = student['skills']
print(type(skill_values), '\nskills: ', skill_values)
