
import  re
from collections import Counter

print(' ')

txt = "Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language"

match = re.match('Python', txt)
print(match)

span = match.span()
print(span)

match2 = re.search('python', txt)
print(match2)

span2 = match2.span()
start, end = span2
substring2 = txt[start:end]
print(substring2)

match3 = re.findall('python', txt, re.I)
print(match3)

#todo Square Bracket
match4 = re.sub('[Pp]ython', 'JS', txt)
print(match4)


txt2 = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. \nT%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.\nI fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
\nD%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

match5 = re.sub('%', '', txt2)

#todo Escape character(\) in RegEx
txt6 = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt6))

reg_pattern = r'[Aa]pple|\d+' # d is a special character which means digits, + mean one or more times
txt_vegetables = 'Apple 123 and banana are fruits q, 1, 2, 3. An old cliche says an apple and apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
match7 = re.findall(reg_pattern, txt_vegetables)
print(match7)

#todo Period(.)
txt8 = 'Apple and banana are fruits. old cliche says'
match8 = r'[Aa].' # this square bracket means a and . means any character except new line
print('task8')
print(re.findall(match8, txt8))

#todo Period(.) One or more times(+)
match9 = r'[a].+' # this square bracket means a and . any character, * any character zero or more times
print(re.findall(match9, txt8))

#todo Zero or many times (*). The pattern could may not occur or it can occur many times.
txt = '''Apple and banana are fruits. old'''
match10 = r'[a].*'  # . any character, * any character zero or more times
print(re.findall(match10, txt))

#todo Zero or one time (?). The pattern may not occur or it may occur once.
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
match11 = r'[Ee]-?mail' # ? means here that '-' is optional
print(re.findall(match11, txt))

#todo Quantifier in RegEx
#We can specify the length of the substring we are looking for in a text, using a curly bracket.
# Let us imagine, we are interested in a substring with a length of 4 characters:

txt = 'This regular expression example was made on September 1,  2024 and revised on September 3, 2024'
match12 = r'\d{4}' # exactly four digits
match13 = r'\d{1,4}' # digits from 1 to 4
print(re.findall(match12, txt))
print(re.findall(match13, txt))

#todo Cart ^
#Starts with:
txt = 'This regular This expression example was made on September 1,  2024 and revised on September 3, 2024'
match14 = r'^This'
print(re.findall(match14, txt))

#Negation = there should be negation—of the findings
match15 = r'[^a-zA-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
print(re.findall(match15, txt))

#todo Home work 1
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

words = re.findall(r'\b\w+\b', paragraph) # Use regex to find all words in the paragraph
word_count = Counter(words) # Count the frequency of each word
#most_common_word = word_count.most_common(1) # Find the most common word
most_common_word = word_count.most_common()
# Count word frequency
for count, word in most_common_word:
    print(f'''({word}, {count}),''')
