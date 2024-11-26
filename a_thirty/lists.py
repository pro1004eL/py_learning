
import math

#todo day 5 "Lists"
print(' ')

#lst = ['item1', 'item2', 'item3', 'item3.2', 'item3', 4, 5]


#rm_ite2 = lst.remove('item3')
#rm_item3 = [item for item in lst if item != 'item3']
#print(rm_item3)

#del lst[:2]



#todo homework
#todo day5 #1,2,3
empty_list= []
lst = ['item1', 'item2', 'item3', 'item4', 'item5']
#print(len(lst))

#todo day5 #4
lst.pop(1)
lst.remove('item4')
#print(lst)

#todo day5 #5,6,7,8,9
mixed_data_types = ['Anton', '33', '173', 'single', 'Ukraine']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#print(it_companies)
#print(len(it_companies))
first_company = it_companies[0]
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index]
last_company = it_companies[-1]
#print('The first company:', first_company, '\nThe middle company:', middle_company, '\nThe last company:', last_company )

#todo day5 #10
it_companies[0] = 'TikTok'
#print(it_companies)

#todo day5 #11
it_companies.insert(1, "Facebook")
#print(it_companies)

#todo day5 #12, 13
#Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
insert_middle_com = it_companies.insert(middle_index, 'IT company')
it_companies[1] = it_companies[1].upper()
#print(it_companies)

#todo day5 #14,15
conct = '#;  '.join(it_companies)

check1 =  'FACEBOOK' in it_companies, 'Google' in it_companies
#print(check1)

#todo day5 #16,17
it_companies.sort()
#print(it_companies)

#todo day5 #18,19
remv = it_companies[3:]
#print(remv)
remv2 = it_companies[:-3]
#print(remv2)

#todo day5 #20,21,22
remv3 = it_companies.remove(it_companies[0])
#print(it_companies)
middle_company = len(it_companies) // 2
remv4 = it_companies.remove(it_companies[middle_company])
#print(it_companies)
remv5 = it_companies.remove(it_companies[-1])
#print(it_companies)

#todo day5 #24
it_companies.clear()
#print(it_companies)

#todo day5 #25
del it_companies
#print(it_companies)

#todo day5 #26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
#list6 = front_end + back_end
front_end.extend(back_end)
#print(front_end)

#todo day5 #27
full_stack = front_end.copy()
#print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
#print(full_stack)


#todo day5 Level 2 #1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(ages, '\n' f'Min age: {min_age}', '\n' 'Max age: ', max_age )

#todo day5 Level 2 #2
n = len(ages)

# Calculate the median
if n % 2 == 1:
    median = ages[n // 2] # If odd, the median is the middle element
else:
    median = (ages[n // 2-1] + ages[n // 2]) / 2 # If even, the median is the average of the two middle elements

print('Median age: ',median)

sum_age = sum(ages)
count_list = len(ages)
average_age = sum_age / count_list
print('average_age: ', average_age)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Calculate the average age
total_sum = sum(ages)
num_elements = len(ages)
average_age = total_sum / num_elements

# Find the minimum and maximum ages
min_age = min(ages)
max_age = max(ages)

# Calculate the absolute differences
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

print("Average age:", average_age)
print("Min age:", min_age)
print("Max age:", max_age)
print("Absolute difference between min and average:", min_diff)
print("Absolute difference between max and average:", max_diff)

#todo day5 Level 3
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
]

count_mid = len(countries) // 2
middle_counties = countries[count_mid]
print(middle_counties)

n2 = len(countries)
mid2_counties = (n2+1) // 2
first_country_list = countries[:mid2_counties]
second_country_list = countries[mid2_counties:]
print('first half:', first_country_list)
print('second half: ', second_country_list)

#todo lvl 3 #3
counties2 = ['China', 'Ukraine', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_contr, *scandinav = counties2
print('first_country:', first_country, '\n' f'second_country: {second_country}', '\n' f'third_contry: {third_contr}')
print('scandinav: ', scandinav)

adwentures_of_tom_sawer = '''Tom gave up the brush with reluctance in his face but alacrity in his heart. 
And while the late steamer "Big Missouri" worked and sweated in the sun, the retired artist sat on a barrel in the shade close by,
 dangled his legs, munched his apple, and planned the slaughter of more innocents. 
 There was no lack of material; boys happened along every little while; 
 they came to jeer, but remained to whitewash. 
 By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; 
 and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, 
 hour after hour. And when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, 
 Tom was literally rolling in wealth. '''

# task 07 - day 4
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
# розділяємо текст по кінцю речення:
sentences = adwentures_of_tom_sawer.split('.')
#adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in adwentures_of_tom_sawer.split('.') if sentence]
# створюємо пустий список для збереження результату:
adwentures_of_tom_sawer_sentences = []
# ітеруємо рядки за допомогою циклу for:
for sentence in sentences:
    # видаляємо зайві пробіли з початку та кінця кожного рядка:
    cleaned_sentence = sentence.strip()
    if cleaned_sentence:
        # добавляємо рядки до кінцевого списку
        adwentures_of_tom_sawer_sentences.append(cleaned_sentence)

print(adwentures_of_tom_sawer_sentences)

# task 09 - day 4
""" Перевірте чи починається якесь речення з "By the time".
"""

# Initialize a flag to check if any sentence starts with "By the time"
starts_with_phrase = False

for phrase in adwentures_of_tom_sawer_sentences:
    if phrase.startswith('By the time'):
        starts_with_phrase = True
        print('Task 09')
        print("There is a sentence that starts with 'By the time'.")
# якщо сходження немає, виводимо помилку
#assert starts_with_phrase, "В тексті не має речення яке починається з 'By the time'"

# print('Task 09')
# if starts_with_phrase:
#     print("There is a sentence that starts with 'By the time'.")
# else:
#     print("No sentence starts with 'By the time'.")

# =============================
def extract_test_case_names(log_lines):
    test_case_names = []

    # Iterate through each line in the input list
    for line in log_lines:
        # Check if 'TestCase:' exists in the line
        if 'TestCase:' in line:
            # Split the line by 'TestCase: ' and take the second part (which contains the test name)
            parts = line.split('TestCase: ')
            # The test name will be after 'TestCase:', strip any extra spaces or newlines
            test_name = parts[1].strip()
            # Append the test name to the result list
            test_case_names.append(test_name)

    return test_case_names


# Example usage:
log_lines = [
    '2023-04-27 15:30:45 - TestCase: login_successful',
    '2023-04-27 15:35:12 - TestCase: invalid_password',
    '2023-04-27 16:00:00 - TestCase: password_reset'
]

test_cases = extract_test_case_names(log_lines)
print(test_cases)


