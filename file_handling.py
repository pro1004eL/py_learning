import os
import json
import csv

print('')

f = open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt')
print(f)

txt = f.read()
print(type(txt))
print(txt)
f.close()

# only 1 line
f = open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt')
line1 = f.readline()
print(type(line1))
print(line1)
f.close()

# str => list
f = open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt')
line1 = f.readlines()
print(type(line1))
print(line1)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt')
line1 = f.read().splitlines()
print(type(line1))
print(line1)
f.close()

# There is a new way of opening files using with - closes the files by itself. Let us rewrite the the previous example with the with method:
with open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt') as f:
    lines = f.readlines()
    print(type(lines))
    print('test', lines)

# Opening Files for Writing and Updating
# with open('/Users/Anton/python/python_learning/py_30_Days/reading_file_example.txt', 'a') as f:
#     f.write('This text has  end32131213123')
#
# with open('/Users/Anton/python/python_learning/py_30_Days/write_file_example.txt', 'w') as f:
#     f.write('This text will be written in a newly created file')

#todo Deleting Files

if os.path.exists('/Users/Anton/python/python_learning/py_30_Days/write_file_example.txt'):
    os.remove('/Users/Anton/python/python_learning/py_30_Days/write_file_example.txt')
else:
    print('The file does not exist')

# we use three quotes and make it multiple line to make it more readable
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"
person_json = '''{
    "name":"Anton",
    "country":"Ukraine",
    "city":"Ovruch",
    "skills":["JavaScrip", "React","Python"]
}'''
print(type(person_json))

#todo Changing JSON to Dictionary
person_dic = json.loads(person_json)
print(type(person_dic))
print(person_dic)
print(person_dic['city'])

#todo Changing Dictionary to JSON
# python dictionary
person = {
    "name":"Anton",
    "country":"Ukraine",
    "city":"Ovruch",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json_to_dic = json.dumps(person, indent=4)
print(type(person_json_to_dic))
print(person_json_to_dic)

#todo File with csv Extension

with open('/Users/Anton/python/python_learning/py_30_Days/csv_exampl.csv') as f_csv:
    csv_reader = csv.reader(f_csv, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {', '.join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} is a lerner. He is from {row[2]}, his age: {row[3]}')
            line_count += 1
    print(f'Number of lines: {line_count}')


#todo HW_level1_#1

# Open and read the file
with open('/Users/Anton/python/python_learning/py_30_Days/obama_speech.txt', 'r') as obama:
    text1 = obama.read()
    # Count the number of lines
    lines = text1.split('\n')
    num_lines = len(lines)
    print('Count Obama lines in the text: ', num_lines)

    # Count the number of words
    words = text1.split()
    num_words = len(words)
    print('Count words in the Obama text: ', num_words)

#todo HM_2

def most_spoken_languages(file_path, num_languages):
    # Read the JSON data from the file
    with open(file_path, 'r') as file:
        countries_data = json.load(file)

    # Extract all languages from the JSON data and count their occurrences
    language_counts = {}
    for country in countries_data:
        for language in country['languages']:
            if language in language_counts:
                language_counts[language] += 1
            else:
                language_counts[language] = 1

    # Convert the dictionary to a list of tuples and sort it by count in descending order
    sorted_languages = sorted(language_counts.items(), key=lambda x: x[1], reverse=True)

    # Return the top most spoken languages
    return sorted_languages[:num_languages]

# Replace 'countries.json' with the actual path to your JSON file
file_path = '/Users/Anton/python/python_learning/py_30_Days/counties_data.json'
#top_languages = most_spoken_languages(file_path, num_languages)

print(most_spoken_languages(file_path, 6))

#todo home_work #3

def most_country_population(file_path, thenumber):
    with open(file_path, 'r') as population_file:
        country_list = json.load(population_file) # json => list

    # Extract the country name and population, and create a list of tuples
    #A list comprehension is used to extract each country's name and its population, creating a list of dictionaries in the format {'country': country_name, 'population': population}
    country_population = [{'country': country['name'], 'population': country['population']} for country in country_list]


    # Convert the dictionary to a list of tuples and sort it by count in descending order
    #The list of dictionaries is sorted in descending order based on the population using sorted() with a key that sorts by the 'population' field.
    population_sorted = sorted(country_population, key=lambda x: x['population'], reverse=True)

    # Return the top most populated countries
    return population_sorted[:thenumber]

print(most_country_population(file_path,5))







