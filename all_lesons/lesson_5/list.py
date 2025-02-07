
# Level 1
# Declare an empty list
it_companies = []
# Declare a list with more than 5 items
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Find the length of your list
lens_list = len(it_companies)
print('len it companies:', lens_list)
# Get the first item, the middle item and the last item of the list
print('first item:', it_companies[0])
middle_item = lens_list // 2
print('middle item:', it_companies[middle_item])
print('last item:', it_companies[-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Anton", '33', 172, 'single', 'UA']
# Add an IT company to it_companies
it_companies.append("OpenAI")

# Insert an IT company in the middle of the companies list
it_companies.insert(middle_item, "DeepSeek")

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()

# Join the it_companies with a string '#;  '
#it_companies = '#; '.join(it_companies)
#print(it_companies)
# Check if a certain company exists in the it_companies list.
comp = "Oraclee"
if comp in it_companies:
    print(f"Yes, the {comp} company exists in the list")
else:
    print(f"the {comp} company NO exists in the list")
# Sort the list using sort() method
it_companies.sort()
print(it_companies)
# Reverse the list in descending order using reverse() method
it_companies2 = sorted(it_companies, reverse=True)
print(it_companies2)
# Slice out the first 3 companies from the list
print(it_companies[3:])
# Slice out the last 3 companies from the list
print(it_companies[:-3])

# Slice out the middle IT company or companies from the list
middle_item = len(it_companies) // 2
before_middle = it_companies[0:middle_item]
after_middle = it_companies[middle_item+1:]
print(before_middle + after_middle)

# Remove the first IT company from the list
it_companies.remove(it_companies[0])
# Remove the middle IT company or companies from the list
it_companies.remove(it_companies[middle_item])
# Remove the last IT company from the list
it_companies.pop()
# Remove all IT companies from the list
new_list = []
for i in it_companies:
    if i.isprintable():
        new_list.append(i)

for word in new_list:
    it_companies.remove(word)
print('it_companies list:', it_companies)
# Destroy the IT companies list
del it_companies  # totaly delete list

# 26. Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack,
# then insert Python and SQL after Redux.

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
full_stack = front_end.copy()

full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)

# Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19]

# Sort the list and find the min and max age
min_age = min(ages)
max_age = max(ages)
print(f'min_age: {min_age} \nmax_age: {max_age}')

# Add the min age and the max age again to the list
ages.insert(0, min_age)
ages.insert(0, max_age)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
n = len(ages)

# Calculate the median
if n % 2 == 1:
    median = ages[n // 2] # If odd, the median is the middle element
else:
    median = (ages[n // 2-1] + ages[n // 2]) / 2 # If even, the median is the average of the two middle elements

print('Median age: ', median)

# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)

# Find the range of the ages (max minus min)
range_of_ages = max_age - min_age
print(f'range_of_ages: {range_of_ages}')

# Compare the value of (min - average) and (max - average), use abs() method

abs_min = abs(min_age - average_age)
abs_max = abs(max_age - average_age)

print(f'abs_min: {abs_min:.2f} \nabs_max: {abs_max:.2f}')

# Find the middle country(ies) in the countries list
countries = ['China', 'Ukraine', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

middle_country= len(countries) // 2
print(f'middle_country is: {countries[middle_country]}')


countries = ['China', 'Ukraine', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark', 'Polska']

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# Check if the length is even or odd
mid = len(countries) // 2

if len(countries) % 2 == 0:
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    first_half = countries[:mid + 1]
    second_half = countries[mid + 1:]

print("First half:", first_half)
print("Second half:", second_half)


# Unpack the first three countries and the rest as scandic countries.
china, ukraine, usa, *scandic_countries = countries

print(china)
print(ukraine)
print(*scandic_countries)















