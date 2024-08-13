

#task 1

# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print(count)

# for x in range(11):
#     print(x)
# else:
#     print('The loop ended')


#todo 2

# num = 10
# while num >= 0:
#     print(num)
#     num -= 1 # the same num = num - 1
# else:
#     print('Loop ends')
#
# for x in range(10, -1, -1):
#     print(x)
# else:
#     print('The loop FOR ended')
#
# #todo 3
# for i in range(0, 6):
#     print('#' * i) # Print '#' repeated i times
#
# #todo 4
# for h in range(4):          # Outer loop for rows (5 rows)
#     for t in range(15):      # Inner loop for columns (5 columns)
#         print("#", end=' ') # Prints # followed by a space, with end=' ' preventing (предотращать) the default newline after each #.
#     print(' ')                 # Print a newline after each row, Moves to the next line after printing all # characters in a row.
#
# #todo 5
# for w in range(5):
#     print(f'{w} * {w} = {w*w}') #This line showing the multiplication of "w" by itself and displaying the result.
#
# #todo 6
# lst_loop = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
#
# for i in lst_loop:
#     print(i)

#todo 7, 8

for even1 in range(0, 15, 2):
    print(even1)
else:
    print("even end")

for odd1 in range(0, 10):
    if odd1 % 2 != 0:
        print(odd1)



