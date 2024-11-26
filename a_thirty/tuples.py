print(' ')


#todo Day 6
family_members = ('Anton', 'Kostya', 'Katya', 'Tanya', 'Viktor')
print(family_members)

i_am, brother, sister, mama, father = family_members
print(brother)

mid_item = len(family_members) // 2
print('Middle item: ', family_members[mid_item])

first3 = family_members[0:3]
last_three = family_members[-3:]
print(first3, last_three)
print("Kostya" and "Anton" in family_members)