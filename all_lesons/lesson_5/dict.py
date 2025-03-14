# Створення словника зі списками кортежів
# Кожен співробітник має ім'я, прізвище, посаду та рік прийняття на роботу
employees_data = {
    'Іваненко_Іван': ('Іван', 'Іваненко', 'Розробник', 2015),
    'Петренко_Ольга': ('Ольга', 'Петренко', 'Менеджер', 2018),
    'Коваленко_Михайло': ('Михайло', 'Коваленко', 'Дизайнер', 2017),
    # Додайте інші записи за потребою
}

# Додавання нового співробітника
employees_data['Міщенко_Анна'] = ('Анна', 'Міщенко', 'Інженер', 2019)


# Приклад пошуку за критерієм
def find_employees_by_position(position):
    # 2 це iндекс посади у кортежi данних спрiвробiтника
    return [emp_id for emp_id, emp_data in employees_data.items() if emp_data[2] == position]


# Пошук всіх розробників
developers = find_employees_by_position('Розробник')
print(f"Розробники: {developers}")


# Приклад сортування за роком прийняття на роботу
sorted_employees = sorted(employees_data.items(), key=lambda x: x[1][3])

print("\nСортований список за роком прийняття на роботу:")
for employee_id, employee_list in sorted_employees:
    print(f"{employee_id}: {employee_list[3]}")

print('-' * 60)
# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
barsik = {
    'name': 'Barsik',
    'color': 'Black',
    'breed': 'Home',
    'legs': 4,
    'age': 18
}
margosha = {
    'name': 'margosha',
    'color': 'Black',
    'breed': 'Home',
    'legs': 4,
    'age': 12
}

# Create a student dictionary and add first_name, last_name, gender, age,
# marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Tom',
    'last_name': 'Cruse',
    'gender': 'male',
    'age': 4,
    'marital_status': 'milioner',
    'skills': ['python', 'Selenium', 'CSS', 'HTML', 'API', 'Docker', 'SQL', 'Regression testing', 'Postman'],
    'country': 'ua',
    'city': 'Kharkiv',
    'address': 'sumska, 1',
}


# Get the length of the student dictionary
print('lens_student_dict:', len(student))

# Get the value of skills and check the data type, it should be a list
student_skills = student['skills']
print('student_skills:', student_skills)
print(type(student_skills))

# Modify the skills values by adding one or two skills
new_skills = ['HTTP', 'JMeter']
student_skills.extend(new_skills)
print('student_skills:', student_skills)

# Get the dictionary keys as a list
student_keys = list(student.keys())
print('student_keys:', student_keys)
print(type(student_keys))

# Get the dictionary values as a list
student_values = list(student.values())
print('student_keys:', student_values)
print(type(student_values))

# Change the dictionary to a list of tuples using items() method
student_tuples = list(student.items())
print(type(student))
print('student_list_of_tuples:', student_tuples)

# Delete one of the items in the dictionary
print(student)
student.popitem()
print(student)

# Delete one of the dictionaries
print('margo:', margosha)
del margosha
#print('margo:', margosha)  # після видалення словника margosha,повертає помилки NameError


print('-'*60)
#todo  1. Basic Dictionary Operations
#
# Create a dictionary named person with keys: "name", "age", and "city".
person = {
    'name': 'Ronaldo',
    'age': 2005,
    'city': 'NY city'
}

# Add a new key "job" with any value.
person["job"] = 'racer'

# Update the "age" key by increasing its value by 1.
person['age'] = 40

# Delete the "city" key from the dictionary.
print('person:', person)
person.pop('city')
print('person:', person)

#todo  2. Loop Through a Dictionary

# Given a dictionary products = {"apple": 2, "banana": 3, "orange": 1},
# write a loop to print each product and its price in the format: "Product: apple, Price: 2".

products = {"apple": 2, "banana": 3, "orange": 1}

for key, value in products.items():
    print(f'Product: {key}, Price: {value}')

#todo 3. Dictionary Methods Practice

#Create a dictionary of three students with their scores:
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Check if "David" is in the dictionary. If not, add "David" with a score of 88.
if 'David' not in scores:
    scores['David'] = 88
print(scores)

# Get the score of "Bob" safely without causing an error.
bob_scores = scores["Bob"]
print('bob_scores', bob_scores)

# Remove "Charlie" from the dictionary and print the updated dictionary.
scores.pop('Charlie')
print(scores)

#todo  4. Nested Dictionary
#
# Create a dictionary school where each key is a class name ("Class A", "Class B")
# and the value is another dictionary containing student names as keys and their grades as values.

school = {
    "Class A": {
        'Anton': 95,
        'Denny': 15,
        'Ron': 46,
        'Tom': 99,
    },
    "Class B": {
        'Sindy': 99,
        'Katrine': 55,
        'Sofia': 32,
        'Mel': 31,
    }
}


# Add a new student "Emma" with a grade of 90 to "Class A".
school['Class A']['Emma'] = 90
print('class A:', school['Class A'])

# Print all students and their grades from "Class B".
print('class B:', school['Class B'])

#todo 5. Merging Dictionaries
#
# Given two dictionaries:
dict1 = {"a": 1, "b": 22}
dict2 = {"b": 33, "c": 4}

# Merge them into one dictionary and handle duplicate keys by keeping the highest value.
merged_dict = {key: max(dict1.get(key, 0), dict2.get(key, 0)) for key in dict1.keys() | dict2.keys()}
print('merge1:', merged_dict)

#todo 6. Counting Word Frequency

# Write a program that takes a string and counts how many times each word appears, storing the result in a dictionary.
# Example input: "apple banana apple orange banana apple"
# Expected output: {"apple": 3, "banana": 2, "orange": 1}

# fruits = "apple banana apple orange banana apple"
# def counting_words(str):
#     new_dict = {}
#
#     for word in str.split():
#         if word in new_dict:
#             new_dict[word] += 1
#         else:
#             new_dict[word] = 1
#
#     return new_dict
# print(counting_words(fruits))

from collections import Counter

fruits = "apple banana apple orange banana apple"

def counting_words(text):
    return dict(Counter(text.split()))

print(counting_words(fruits))







