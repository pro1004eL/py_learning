# Level 1
# Create an empty tuple
new_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brathers = ('Konstantin', 'Alexandr', 'Artem', 'Viktor', 'Konstantin')
sisters = ('Ira', 'Katya', 'Luba', 'Inna', 'Sofia')

# Join brothers and sisters tuples and assign it to siblings
brat_and_sister = brathers + sisters

# How many siblings do you have?
print('siblings:', len(brat_and_sister))
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Tanya', 'Victor')
family_members = parents + brat_and_sister
print(family_members)


# Level 2
# Unpack siblings and parents from family_members
mather, father, *brathers_and_sisters = family_members

print('-' * 50)
# Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = []
vegetables = []
animal_products = []

food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# Slice out the first three items and the last three items from food_staff_lt list
# Delete the food_staff_tp tuple completely

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if an item exists in tuple:
# Check if 'Estonia' is a nordic country
#
# Check if 'Iceland' is a nordic country
#











