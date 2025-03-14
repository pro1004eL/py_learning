
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

age = [22, 19, 24, 25, 26, 24, 25, 24]


# Exercises: Level 1
# Find the length of the set it_companies
print('it_companies lens:', len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')

# Insert multiple IT companies at once to the set it_companies
elon_companies = {'Tesla', 'SpaceX'}
it_companies.update(elon_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

# What is the difference between remove and discard
'''remove(value) → Raises an error if the value is not found in the set.
discard(value) → Does not raise an error if the value is not found; it simply does nothing.'''


# Exercises: Level 2
a = {19, 22, 24, 20, 25, 26,33}
b = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
join1 = a.union(b)
print('Join A and B:', join1)

# Find A intersection B
inter = a.intersection(b)
print('A intersection B:', inter)

# Is A subset of B
sub = a.issubset(b)
print('Is A subset of B:', sub)

# Are A and B disjoint sets
is_disjoint = a.isdisjoint(b)
print('Are A and B disjoint sets:', is_disjoint)

# Join A with B and B with A
a_with_b = a.union(b)   # (same as union)
b_with_a = b.union(a)
print('Join B with A:', b_with_a)

# What is the symmetric difference between A and B
sm_disjoint = a.symmetric_difference(b)
print('Are A and B symmetric_difference:', sm_disjoint)


# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?


# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.