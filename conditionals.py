
print(' ')

#todo Day 9 #1

# age = float(input('Enter your age: '))
#
# if age >= 18:
#     print('You are old enough to learn to drive.')
# else:
#     not_en = int(18 - age)
#     print(f'You haven\'t 18, you need {not_en} more years to learn to drive.')

#todo Day 9 #2

#my_age = 33
# your_age = float(input('Enter your age: '))
#
#
# if your_age > my_age:
#     diff_age = int(your_age - my_age)
#     print(f'You are {diff_age} years older than me.')
# elif your_age < my_age:
#     diff2 = int(my_age - your_age)
#     print(f'You are {diff2} years younger than me.')
# else:
#     print(f'We have the same {my_age} age.')


#todo Day 9 #3
# enter_num_one = int(input('enter number one: '))
# enter_num_two = int(input('enter number two: '))
#
# if enter_num_one > enter_num_two:
#     print(f'{enter_num_one} is greater than {enter_num_two}')
# elif enter_num_one < enter_num_two:
#     print(f'{enter_num_one} is smaller than {enter_num_two}')
# else:
#     print(f'{enter_num_one} is equal to {enter_num_two}')


#todo Day 9 level 2 #1  Write a code which gives grade to students according to theirs scores

# scores = int(input('enter a score number: '))
#
# if scores >= 0 and scores <= 49:
#     print(f'Your scores {scores}, F')
# elif scores >= 50 and scores <= 59:
#     print(f'Your scores {scores}, D')
# elif scores >= 60 and scores <= 69:
#     print(f'Your scores {scores}, C')
# elif scores >= 70 and scores <= 79:
#     print(f'Your scores {scores}, B')
# elif scores >= 80 and scores <= 100:
#     print(f'Your scores {scores}, A')
# else:
#     print('Please enter a number from 0 to 100')

#todo Lvl_2 #2
#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
user_month = input('Please enter a month when you born: ')
summer = ['June', 'July', 'August']
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']

if user_month in summer:
    print(f'You born in the summer, {user_month}')
elif user_month in autumn:
    print(f'You born in the autumn')
elif user_month in winter:
    print(f'You born in the winter')
elif user_month in spring:
    print(f'You born in the spring')
else:
    print('Please write a correct month')

