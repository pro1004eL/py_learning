# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


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
company = "Coding For All"
contein = company.index('Coding')
#print(contein)

#todo day 4 #11
re = company.replace('Coding', 'Python')
#print(re)

#todo day 4 #12
new_re = 'Python for Everyone'
print(new_re.replace('Everyone', 'All'))

#todo day 4 #13
print(company.split())