# Цикл на строках
word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index += 1


person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ":", value)

# Використання continue для пропуску парних чисел
for i in range(10):
    if i % 2 == 0:
        continue
    print("Непарне число:", i)

print('-'*80)

#todo 6.1
#
# Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

# user_input = set(input('enter any value: '))

# if len(user_input) > 10:
#     print(True)
# else:
#     print(False)

#todo 6.2
#
# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

# while True:
#     user_input = input('enter value with "H/h" symbol: ')
#     if 'h' in user_input.lower():
#         print('Text is correct')
#         break

#todo 6.3

# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = [item for item in lst1 if type(item) == type('str')]

print(lst2)

#todo 6.4
#Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті

some_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,12,13,14,15]

summ_even_numbers = sum([i for i in some_numbers if i % 2 == 0])

print(f'summ_even_numbers: {summ_even_numbers}')

print('-'*30, 'DeepSeek', '-'*30)
# Tasks for "for" Loops
# Print Numbers from 1 to 10
# Write a for loop that prints numbers from 1 to 10.
numbers = [i for i in range(6)]
print(numbers)
#
# Sum of Numbers
# Use a for loop to calculate the sum of numbers from 1 to 100.
sum_numbr = sum([i for i in range(100)])
print(f'sum 100 numbers: {sum_numbr}')
#
# Print Even Numbers
# Write a for loop to print all even numbers between 1 and 20.
even_numbr = [i for i in range(20) if i % 2 == 0]
print(f'even numbers: {even_numbr}')
#
# Multiplication Table
# Write a for loop to print the multiplication table of a number entered by the user
# (e.g., 5 x 1 = 5, 5 x 2 = 10, ..., 5 x 10 = 50).
for i in range(11):
   print(f'5 * {i} = {5 * i}')


#
# Count Vowels in a String
# Use a for loop to count how many vowels (a, e, i, o, u) are in a string provided by the user.

#user_input = input('enter text: ').lower()
def user_input_text(text):

    vowels = "aeiou"
    vowel_count = 0

    for i in text:
        if i in vowels:
            vowel_count += 1

    return vowel_count

#print(user_input_text(user_input))

# Tasks for while Loops
# Print Numbers from 1 to 10
# Write a while loop that prints numbers from 1 to 10.
count = 0
while count < 10:
    print(count)
    count += 1


#
# User Input Validation
# Use a while loop to repeatedly ask the user for a number until they enter a positive number.
# while True:
#     user_text = int(input('enter a positive number: '))
#     if user_text > 0:
#         break
#
# Factorial Calculation
# Write a while loop to calculate the factorial of a number entered by the user (e.g., 5! = 5 x 4 x 3 x 2 x 1 = 120).
import math
#user_number = int(input('enter a positive number: '))
#print(math.factorial(user_number))

#
# Guess the Number Game
# Use a while loop to create a simple guessing game where the user has to guess a predefined number
# (e.g., 7). Provide hints like "Too high" or "Too low" until they guess correctly.
#
# while True:
#     user_num = int(input('enter a positive number: '))
#     predefined_number = 6
#     if user_num > predefined_number:
#         print("Too high")
#     elif user_num < predefined_number:
#         print("Too low")
#     else:
#         print(f'Yes, it is number: {predefined_number}')
#         break

print('-'*30, 'additional task')
grades_1 = {'Анна Коваленко': 92, 'Олег Петров': 85, 'Ірина Сидорова': 78, 'Свирид Свиридович': 99}
grades_2 = {'Анна Коваленко': 90, 'Олег Петров': 85, 'Ірина Сидорова': 80}
def solution(text1, text2):
    # x = {}
    # for key in text1:
    #     if key in text2:
    #         x[key] = text1[key] - text2[key]

    x = {key: text1[key] - text2[key] for key in text1 if key in text2}

    return x

print(solution(grades_1, grades_2))

def solution2(*args, sep="."):

    day, month, year = args

    day_str = f"{day:02d}"  # Ensures two digits (e.g., 1 → "01")
    month_str = f"{month:02d}"  # Ensures two digits (e.g., 2 → "02")
    year_str = str(year)

    x = sep.join([day_str, month_str, year_str])

    return x

print(solution2(11,2,2025, sep='/'))






