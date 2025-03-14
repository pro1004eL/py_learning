#
#todo  Level 1

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(num1, num2):
    return num1 + num2


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return 3,14 * r * r

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    return sum(args)

print(add_all_nums(1,2,3,4,5,))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsium):
    fahrenheit = (float(celsium) * 9.5) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(90))

# Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.


# Write a function called calculate_slope which return the slope of a linear equation
# Quadratic equation is calculated as follows: ax² + bx + c = 0.
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)

some_lst = ['one', 'two', 'three']

print_list(some_lst)

# 9. Declare a function named reverse_list.
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(array):
    return list(reversed(array))

some_arrey = [10, 20 , 23, 33, 21, 15, 1]
print(reverse_list(some_arrey))

# 10. Declare a function named capitalize_list_items.
# It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lst):
    # new_list = []
    # for i in lst:
    #     if isinstance(i, str):  # the same as type(i) == str
    #
    #         new_list.append(i.capitalize())

    new_list = [i.capitalize() for i in lst if isinstance(i, str)]

    return new_list

list_c = ['tear', 'tease', 'text', 22, True, None, 'Quine', 'WWW']

print(capitalize_list_items(list_c))

# 11. Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.
def add_item(lst: list, add_i):
    lst.append(add_i)
    return lst


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))     # [2, 3, 7, 9, 5]

# 12. Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.
def remove_item(lst:list, i_param):
    lst.remove(i_param)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 7))  # [2, 7, 9]

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    x = sum([i for i in range(number+1)])
    return x


print('number_5:', sum_of_numbers(5))  # 15
print('number_10:', sum_of_numbers(10))  # 55
print('number_100:', sum_of_numbers(100))  # 5050

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    x = sum([i for i in range(number) if i % 2 != 0])
    return x

print('Sum_odd_numbers_5:', sum_of_odds(5))

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    x = sum([i for i in range(number) if i % 2 == 0])
    return x

print('Sum_even_numbers_5:', sum_of_even(5))

#todo Level 2

# 1. Declare a function named evens_and_odds .
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(integer):
    even_num = []
    odd_num = []
    for i in range(integer):
        if i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)

    return f'The number of odds are {len(odd_num)}. \nThe number of evens are {len(even_num)}.'

print(evens_and_odds(543))
    # The number of odds are 50.
    # The number of evens are 51.

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i  # fact = fact * i
    return fact

print(f'factorial of the number 3:', factorial(3))

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(value):
    return not bool(value)

print('is empty?:', is_empty(3))

# 4. Write different functions which take lists.
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).


#todo Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n: int) -> list:

    if type != int:
        print(f'find_primes input param is not int {type(n)}, {n}')

    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(is_prime(3))

# 2. Write a functions which checks if all items are unique in the list.
def unique_items(lst: list):
    to_set = set(lst)
    if len(lst) == len(to_set):
        return 'all items are unique in the list'
    else:
        return 'items are NOT unique in the list'

print(unique_items([1,2,3,4,5,6,7, "reer"]))

# 3. Write a function which checks if all the items of the list are of the same data type.
def same_data_type(lst: list):
    """
    :param lst:
    :return:
    """

    firt_item_type = type(lst[0])
    x = all([isinstance(i, firt_item_type) for i in lst])
    return x

print('Is all the items of the list are of the same data type:', same_data_type([1,23,4,5, 123]))


# 4. Write a function which check if provided variable is a valid python variable
def check_var_name(var: str):
    return var.isidentifier()

print('Is a valid varible name:', check_var_name('__ewew'))

#todo 5. Go to the data folder and access the countries-data.py file.

# Create a function called the most_spoken_languages in the world.
# It should return 10 or 20 most spoken languages in the world in descending order (у зворотньому порядку)
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

with open("/Users/Anton/python/python_learning/py_30_Days/all_lesons/lesson_7/countries-data.py", 'r') as file:
    content = file.read()

import json
from collections import Counter

countries_data = json.loads(content)
language_counter = Counter()

for country in countries_data:
    for language in country["languages"]:
        language_counter[language] += 1

top_10_languages = language_counter.most_common(10)

print('the most_spoken_languages in the world', top_10_languages)


#todo 6. *args and **kwargs

def sum_all_numbers(number_one, *numbers, ignore_num, **kwargs):

    print(number_one)
    print(numbers)
    print(ignore_num)

    new_numbers = sum([k for k in numbers if k != ignore_num])
    new_numbers = new_numbers + number_one

    if kwargs.get('double_all'):
        return new_numbers * 2

    return new_numbers

list_of_num = list(range(122, 133))

print('sum numbers:', sum_all_numbers(*list_of_num, ignore_num=132, double_all='313'))












