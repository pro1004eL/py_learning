import random
import string

print(' ')

#todo Day_14 "Comprehencion"
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

number3 = [(i, 1, i**2, i**3) for i in range(10)]
for row in number3:
    print(row)

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
