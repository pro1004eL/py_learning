
import  re

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

match4 = re.sub('[Pp]ython', 'JS', txt)
print(match4)

txt2 = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. \nT%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.\nI fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
\nD%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

match5 = re.sub('%', '', txt2)
print(re.split('\n', ))

