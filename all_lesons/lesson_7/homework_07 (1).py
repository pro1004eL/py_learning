# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    print('task 1')

    # Complete the while loop condition.
    while multiplier <= 10:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15...


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_num(x,y):
    return x + y

print(f'Task 2 \nSum of the numbers 2+3: {sum_two_num(2,3)}')

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avr_num(lst_numbers):
    if len(lst_numbers) == 0:
        return 0
    return sum(lst_numbers) / len(lst_numbers)

some_lst_num = [1,2,3,4,5,6]
print(f'Task 3 \nThe averange number of the list {some_lst_num}: {avr_num(some_lst_num)}')

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def rever_str(str):
    return str[::-1]

some_str = "Tom Riddle, Harry Potter"
print(f'Task 4 \nThe reverse for string "{some_str}": "{rever_str(some_str)}"')

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(lst):
    if not lst:
        return ""
    longest = max(lst, key=len)
    return longest

list_for_long = ['word1', 'word22', 'word333']
print(f'Task 5 \nThe longest word in the list: {longest_word(list_for_long)}')


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print('\ntask 6')
print(find_substring(str1, str2))  # поверне 7

print('task 6.2')
str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# task 8
# task 9
# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
# task 7-10 (1)
#  check that all people in modified list with records indexes 6, 10, 13 have age >= 30.

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

def check_age_thirty(index1, index2, index3):

    thirty_age = all([people_records[index][2] >= 30 for index in (index1, index2, index3)])

    if thirty_age:
        return 'All users have age >= 30'
    else:
        return 'Not all users have age >= 30'


print('\ntask 7\n', check_age_thirty(3,1,2))

# task 7-10 (2)
# Exists some car data with color, year, engine_volume, car type , price
# We have search_criteria as tuple of ( year>= , engine_volume >= , price<=)
# write code that will help us to get cars that satisfy search_criteria.
# Cars should be sorted by price ascending.
# We should print up to five (5) first found elements
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

def search_cars(min_year, min_engine_value, max_price):
    '''

    :param min_year:
    :param min_engine_value:
    :param max_price:
    :return:
    '''

    finding_cars = [(car, *data) for car, data in car_data.items()
                     if data[1] >= min_year and data[2] >= min_engine_value and data[4] <= max_price]

    sorting_cars_by_price = sorted(finding_cars, key=lambda x: x[5])

    if not sorting_cars_by_price:
        print('No matching cars.')
    else:
        for car in sorting_cars_by_price[:5]:
            print(f"{car[0]}: Color: {car[1]}, Year: {car[2]}, Engine Volume: {car[3]}, Type: {car[4]}, Price: {car[5]}")

print('Task 10')
search_cars(2033, 1.6, 36000)









