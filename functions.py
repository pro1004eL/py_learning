
import math
import random
import mymodule
import string

print(' ')
# def sum_of_num(n):
#     total = 0
#     for i in range(n+1):
#         total += i
#         print(i)
#         print(total)
#         print('end')
#     print(total)
# print(sum_of_num(10))


#todo #1
def add_two_numbers(n1, n2):
    total = n1 * n2
    return total

#print('summ of two numbers:', add_two_numbers(2, 3))


#todo #2
def area_of_circle(r):
    p = math.pi
    circle_area = round(p * r * r, 2)
    return circle_area

#print( '\n' 'area_of_circle: ', area_of_circle(5), '\n')

#todo #3
def add_all_nums(*numb):
    if not all(isinstance(i, (int, float)) for i in numb):
        return 'All parameters should be numbers. Please enter a number.'
    total = sum(numb)
    return total

#print('total:', add_all_nums(25,12,1231312313))

#todo #4
def convert_celsius_to_fahrenheit(c):
    if not (isinstance(c, (int, float))):
        return 'Please enter a number.'
    c_to_f = c * (9/5) + 32
    return c_to_f
#print('Temperature converted to °F: ', convert_celsius_to_fahrenheit(27))

#todo #5
def season(month):
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August']
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    if month in spring:
        return f'Your {month} month in the Spring'
    elif month in summer:
        return f'Your {month} month in the Summer'
    elif month in autumn:
        return f'Your {month} month in the Autumn'
    elif month in winter:
        return f'Your {month} month in the Winter season'
    else:
        return"Please enter a month."

#print(season('November'))

#todo #8
def print_list(*lst):
    for i in lst:
        print(i)

#print_list('test1', 'test2', 'test3')

#todo #9
def reverse_list(arg):
    return arg[::-1]

#print(reverse_list([1, 2, 3, 4, 18, 10]))
#print(reverse_list(['five', '4', 'two', 'ten']))

#todo #10
def capitalize_list_items(lst):
    capital_list = []
    for item in lst:
        capital_list.append(item.capitalize())
    return capital_list

print(capitalize_list_items(['centavr', 'ded', 'game']))

#todo #11
def add_item(list, item):
    list.append(item)
    return list

print((add_item([123, '323'], 16)))

#todo #12
def remove_item(list, rem_item):
    list.remove(rem_item)
    return list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9, 124, 32, 66]
print(remove_item(numbers, 32))

#todo #13
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total = total + i
    return total

print(sum_of_numbers(100))

#todo $14
# def sum_of_odds(o):
#     total = 0
#     for odd in range(o+1):
#         if odd % 2 != 0:
#             total = total + odd
#     return total
#
# print(sum_of_odds(10))

#todo $15
# def sum_of_evens(o):
#     total = 0
#     for even in range(o+1):
#         if even % 2 == 0:
#             total = total + even
#     return total
#
# print(sum_of_evens(10))

#todo Lvl_2 #1
def evens_and_odds(num):
    total_odd = 0
    total_even = 0
    for i in range(1, num+1):
        if i % 2 == 0:
            total_even += 1
        else:
            total_odd += 1

    print('Even numbers: ', total_even)
    print('Odd numbers: ', total_odd)

print(evens_and_odds(100))

#todo Lvl_3 #2
def unique_item(lst):
    return len(lst) == len(set(lst))

#print(unique_item(['test', 'test2', 'test3', 1, 2]))

#todo Lvl_3 #3
def data_type(lst):
    if not lst:
        return True

    first_item_type = type(lst[0])
    for item in lst:
        if type(item) != first_item_type:
            return False
    return True

print(data_type([1, 2, '3']))


#=================================#=================================#=================================
print(' \n')
#todo  Day 13 Modules Lvl_1 #1

def random_user_id():
    characters = string.ascii_lowercase + string.digits
    user_id = ''.join(random.choice(characters) for _ in range(6))
    return user_id

print(random_user_id())

#help(string)

def random_num2(n1, n2):
    return random.randint(n1, n2)

print(random_num2(2,12))

def random_user_id2():
    characters2 = string.ascii_lowercase + string.digits
    user_id = ''.join(random.choices(characters2, k=5))
    return user_id

print(random_user_id2())

#todo  Day 13 Modules Lvl_1 #2
def user_id_gen_by_user():
    num_characters = int(input('Please enter a number of characters: '))
    num_iterations = int(input('Please enter a number of iterations: '))
    characters = string.ascii_letters + string.digits


    for i in range(num_iterations):
        user_id = ''.join(random.choices(characters, k=num_characters))
        print(user_id)




print(user_id_gen_by_user())









