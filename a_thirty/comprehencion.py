import random
import string

print(' ')

#todo Day_13 "Comprehencion"
even_numbers = [i for i in range(45) if i % 2 == 0]


#todo #1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
only_positive_num = [i for i in numbers if i <= 0]
print(only_positive_num)

#todo #2
list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
dimensional_list = [i for row in list_of_lists for i in row]
print(dimensional_list)

def dimension3():
    list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

    flattened_list = []
    for sublist in list_of_lists:
        for inner_list in sublist:
            for item in inner_list:
                flattened_list.append(item)
    print(flattened_list)

print(dimension3())

#todo #3

number3 = [(i, 1, i**2, i**3) for i in range(4)]
for row in number3:
    print(row)
print('task 03')
print(number3)

#todo #4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

next_level = [[c, c[:3].upper(), capital] for sub_list in countries for c, capital in sub_list]

print(next_level)



# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#
# flattened_list = []
#
# for sublist in countries:
#     for country, capital in sublist:
#         country_upper = country.upper()
#         country_abbr = country[:3].upper()
#         capital_upper = capital.upper()
#         flattened_list.append([country_upper, country_abbr, capital_upper])
#
# print(flattened_list)

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

list2 = []

for item in lst1:
    if type(item) == type('str'):
        list2.append(item) # Create a new list that contains only the string variables from lst1

print(list2)

# Create a new lst2 that contains only the string variables from lst1
lst3 = [item for item in lst1 if isinstance(item, str)]

print(lst3)
