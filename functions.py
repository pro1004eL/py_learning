
import math

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

print('total:', add_all_nums(25,12,1231312313))

#todo #4
def convert_celsius_to_fahrenheit(c):
    if not (isinstance(c, (int, float))):
        return 'Please enter a number.'
    c_to_f = c * (9/5) + 32
    return c_to_f
print('Temperature converted to °F: ', convert_celsius_to_fahrenheit(27))

#todo #5
def season(month):
    spring = ['March', 'April', 'May']
    summer = ['June', 'July', 'August']
    autumn = ['September', 'October', 'November']
    winter = ['December', 'January', 'February']
    if month in spring:
        return f'You {month} month in the Spring'
    elif month in summer:
        return f'You {month} month in the Summer'
    elif month in autumn:
        return f'You {month} month in the Autumn'
    elif month in winter:
        return f'You {month} month in the Winter'
    else:
        return"Please enter a month."

print(season('November'))

#todo #6













