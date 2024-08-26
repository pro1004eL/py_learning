# This is a sample Python script.
import datetime
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

print(' ')

#todo day 4 #1
upText =  ['Thirty', 'Days', 'Of', 'Python']
thitry = ' '.join(upText)
#print(thitry)

#todo day 4 #2
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding = 'Coding'
code_for = 'For'
all = 'All'
#print(f'{coding} {code_for} {all}')


#todo day 4 #5
#print(len(company), '= lens of the "company" var')

#todo day 4 #6, 7
#print(company.upper() +' = upper and lower = '+ company.lower())

#todo day 4 #8
#capital = company.capitalize()
# title = company.title()
# swapca = company.swapcase()
# print(capital +' '+ title +' '+ swapca)

#todo day 4 #9
#sli = company[6:]
#print(sli)

#todo day 4 #10
#company = "Coding For All"
#contein = company.index('Coding')
#print(contein)

#todo day 4 #11
#re = company.replace('Coding', 'Python')
#print(re)

#todo day 4 #12
new_re = 'Python for Everyone'
#print(new_re.replace('Everyone', 'All'))

#todo day 4 #13
#print(company.split())

#todo day 4 #14
soc_networks = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
#print(soc_networks.split())

#todo day 4 #15
#print(company[10])

#todo day 4 #18,19
#Create an acronym or an abbreviation for the name 'Python For Everyone'.
# abbrev = ''.join(word[0] for word in new_re.split())
# print(abbrev.upper())
#
# abb2 = ''.join(word[0] for word in company.split())
# print(abb2)

#todo day 4 #20,21
#Use index to determine the position of the first occurrence of C in Coding For All.
# company2 = "Coding For All"
# sub_se = 'F'
# sub_i = 'i'
# print(company2.index(sub_se))
# print(company2.rindex(sub_i))

#todo day4 #23,24
text22 =  'You cannot end a sentence with because because because is a conjunction'
sub_22 = 'because'
# print(text22.index(sub_22))
# print(text22.rindex(sub_22))

#todo day4 #25
#Slice out the phrase 'because because because' in the following sentence: ''
# sub_25 = 'because because because'
# cut_start = text22.index('because')
# cut_end = cut_start + len(sub_25)
# slice_out = text22[:cut_start] + text22[cut_end:]
# print(slice_out)

#todo day4 #28,29
#Does ''Coding For All' start with a substring Coding?
# company2 = "Coding For All"
# print(company2.startswith('Coding'))
# print(company2.endswith('coding'))

#todo day4 #30
#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
# str_ciding = '   Coding For All      '
# print(str_ciding.strip(' '))

#todo day4 #31
# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True

#todo day4 #32
#['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# librarys = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# print(' / '.join(librarys))

#todo day4 #33
#print('I am enjoying this challenge. \nI just wonder what is next.')

#todo day4 #34
list33 = 'Name \tAge \tCountry \tCity \nAsabeneh \t250 \tFinland \tHelsinki'
print(list33)

