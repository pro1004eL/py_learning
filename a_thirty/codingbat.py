import math

# 1. Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) <= 1:
        return str

    midle = str[1:-1]

    return str[-1] + midle + str[0]


# print(front_back('code'))
# print(front_back('a'))
# print(front_back('ab'))
# print(front_back('abc'))
# print(front_back(''))
# print(front_back('Chocolate'))
# print(front_back('aavJ'))
# print(front_back('hello'))

# 2.# Given a string, we'll say that the front is the first 3 chars of the string.
# If the string length is less than 3, the front is whatever is there.
# Return a new string which is 3 copies of the front.

def front3(str):
    three = str[0:3]

    return three + three + three


# front3('Java') → 'JavJavJav'	'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'	'ChoChoCho'
# front3('abc') → 'abcabcabc'	'abcabcabc'
# front3('abcXYZ') → 'abcabcabc'	'abcabcabc'
# front3('ab') → 'ababab'	'ababab'
# front3('a') → 'aaa'	'aaa'
# front3('') → ''	''

## 3.
#Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
    return ((abs(n - 100) <= 10) or (abs(n - 200) <= 10))


#near_hundred(93) → True	True	OK
# near_hundred(90) → True	True	OK
# near_hundred(89) → False	False	OK
# near_hundred(110) → True	True	OK
# near_hundred(111) → False	False	OK
# near_hundred(121) → False	False	OK
# near_hundred(-101) → False	False	OK
# near_hundred(-209) → False	False	OK
# near_hundred(190) → True	True	OK
# near_hundred(209) → True	True	OK
# near_hundred(0) → False	False	OK
# near_hundred(5) → False	False	OK
# near_hundred(-50) → False	False	OK
# near_hundred(191) → True	True	OK
# near_hundred(189) → False	False	OK
# near_hundred(200) → True	True	OK
# near_hundred(210) → True	True	OK
# near_hundred(211) → False	False	OK
# near_hundred(290) → False	False

# 4. We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20.
# Return True if we are in trouble.

def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)


# parrot_trouble(True, 6) → True	True	OK
# parrot_trouble(True, 7) → False	False	OK
# parrot_trouble(False, 6) → False	False	OK
# parrot_trouble(True, 21) → True	True	OK
# parrot_trouble(False, 21) → False	False	OK
# parrot_trouble(False, 20) → False	False	OK
# parrot_trouble(True, 23) → True	True	OK
# parrot_trouble(False, 23) → False	False	OK
# parrot_trouble(True, 20) → False	False	OK
# parrot_trouble(False, 12) → False	False

# 5. The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# sleep_in(False, False) → True	True	OK
# sleep_in(True, False) → False	False	OK
# sleep_in(False, True) → True	True	OK
# sleep_in(True, True) → True	True


#6. Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.

def diff21(n):
    diff = 21 - n

    if diff >= 0:
        return diff

    else:
        return (n - 21) * 2


#
# diff21(19) → 2	2	OK
# diff21(10) → 11	11	OK
# diff21(21) → 0	0	OK
# diff21(22) → 2	2	OK
# diff21(25) → 8	8	OK
# diff21(30) → 18	18	OK
# diff21(0) → 21	21	OK
# diff21(1) → 20	20	OK
# diff21(2) → 19	19	OK
# diff21(-1) → 22	22	OK
# diff21(-2) → 23	23	OK
# diff21(50) → 58	58

# 7. Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    if a == b:
        return (a + b) * 2

    return a + b


# sum_double(1, 2) → 3	3	OK
# sum_double(3, 2) → 5	5	OK
# sum_double(2, 2) → 8	8	OK
# sum_double(-1, 0) → -1	-1	OK
# sum_double(3, 3) → 12	12	OK
# sum_double(0, 0) → 0	0	OK
# sum_double(0, 1) → 1	1	OK
# sum_double(3, 4) → 7	7

# 8. Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a > 0 and b < 0) or (a < 0 and b > 0)


# pos_neg(1, -1, False) → True	True	OK
# pos_neg(-1, 1, False) → True	True	OK
# pos_neg(-4, -5, True) → True	True	OK
# pos_neg(-4, -5, False) → False	False	OK
# pos_neg(-4, 5, False) → True	True	OK
# pos_neg(-4, 5, True) → False	False	OK
# pos_neg(1, 1, False) → False	False	OK
# pos_neg(-1, -1, False) → False	False	OK
# pos_neg(1, -1, True) → False	False	OK
# pos_neg(-1, 1, True) → False	False	OK
# pos_neg(1, 1, True) → False	False	OK
# pos_neg(-1, -1, True) → True	True	OK
# pos_neg(5, -5, False) → True	True	OK
# pos_neg(-6, 6, False) → True	True	OK
# pos_neg(-5, -6, False) → False	False	OK
# pos_neg(-2, -1, False) → False	False	OK
# pos_neg(1, 2, False) → False	False	OK
# pos_neg(-5, 6, True) → False	False	OK
# pos_neg(-5, -5, True) → True	True


# 9. Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True

    else:
        return False


# makes10(9, 10) → True	True	OK
# makes10(9, 9) → False	False	OK
# makes10(1, 9) → True	True	OK
# makes10(10, 1) → True	True	OK
# makes10(10, 10) → True	True	OK
# makes10(8, 2) → True	True	OK
# makes10(8, 3) → False	False	OK
# makes10(10, 42) → True	True	OK
# makes10(12, -2) → True	True

class Name:
    def __init__(self, name):
        self.name = name


my_name = Name('Anton')

print(my_name.name)

class Calculator:
    def add(self, x, y):
        return x + y


calc = Calculator()

print(calc.add(3, 5))
print(calc.add("Ded ", "ot Moroz"))

print('---' * 50)

# Задача. Бібліотека

class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title


class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def get_books(self):
        return self.books

book1 = Book('A.C. Doile', 'Sherlok Holms')
book2 = Book('A.C. Doile', 'Sherlok Holms 2.0')

libre = Library()

libre.add_book(book1)
libre.add_book(book2)

books = libre.get_books()

for book in books:
    print(f'Book {book.title} written by {book.author}')

# Задача. Банківський рахунок
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

bank_acc = BankAccount(53213, 1000)

bank_acc.set_account_number(777)
bank_acc.set_balance(1000000)

print("Account number:", bank_acc.get_account_number())
print("Account balance:", bank_acc.get_balance())


# e[ample 2
class Vehicle:
    def __init__(self, color):
        self.color = color

class Car(Vehicle):
    def __init__(self, color, model, wheels):
        super().__init__(color)
        self.model = model
        self.wheels = wheels

my_car = Car(color="Blue", model="Honda", wheels=4)
print(my_car.model, my_car.color)


# String tasks
# 1.
def make_tags(tag, word):
    return f"<{tag}>{word}</{tag}"

print(make_tags('i', 'Yay') )

# 2.
def make_out_word(out, word):
  return (out[:2] + word + out[2:])

print(make_out_word('<<>>', 'Yay'))

# 3.
def extra_end(str):
  return str[-2:]*3

#extra_end('Hello') → 'lololo'	'lololo'	OK
# extra_end('ab') → 'ababab'	'ababab'	OK
# extra_end('Hi') → 'HiHiHi'	'HiHiHi'	OK
# extra_end('Candy') → 'dydydy'	'dydydy'	OK
# extra_end('Code') → 'dedede'

# 4. irst_two('abcdefg') → 'ab'
def first_two(str):
  return str[:2]

print(first_two('abcdefg'))

# 4.
def first_half(str):
  half = len(str)//2
  return str[:half]

# first_half('WooHoo') → 'Woo'	'Woo'	OK
# first_half('HelloThere') → 'Hello'	'Hello'	OK
# first_half('abcdef') → 'abc'	'abc'	OK
# first_half('ab') → 'a'	'a'	OK
# first_half('') → ''	''	OK
# first_half('0123456789') → '01234'	'01234'	OK
# first_half('kitten') → 'kit'

# 5.
def without_end(str):
  return str[1:-1]

# without_end('Hello') → 'ell'	'ell'	OK
# without_end('java') → 'av'	'av'	OK
# without_end('coding') → 'odin'	'odin'	OK
# without_end('code') → 'od'	'od'	OK
# without_end('ab') → ''	''	OK
# without_end('Chocolate!') → 'hocolate'	'hocolate'	OK
# without_end('kitten') → 'itte'	'itte'	OK
# without_end('woohoo') → 'ooho'

# 6.



print('-' * 30, "lesson 4", '-' * 30)
print(11 / 3)
print(round(11 / 3)) # округлення звичайне
print(int(11 / 3)) # округлення вниз
print(math.ceil(11 / 3)) # округлення вгору

original_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
partial_list = original_list[::2]  # Вибираємо елементи з кроком 2
print(partial_list)


name = 'Anton Kolomiiets Viktorovich'

wer = name.split(' ')

print(wer)
print(wer[1])
print(wer[1][0:4])

index = 0
for second in wer:
    new_element = f'this is element: {second} and index: {index}'
    print(new_element)
    index += 1


# Список рядків
list_str = ["apple", "orange", "banana"]

# Об'єднання рядків зі списку за допомогою роздільника ','
alls = ','.join(list_str)

print(alls)

string = "1,2,3"
bool_var = bool(string)
print(type(bool_var))


print('-' * 30, "lesson 4", '-' * 30)

def solution(test_string):
    if 'TestCase:' in test_string:
        # Split the string by 'TestCase: ' and take the second part (which contains the test name)
        parts = test_string.split('TestCase: ')
        # The test name will be after 'TestCase:', strip any extra spaces or newlines
        test_name = parts[1].strip()
        return test_name
    else:
        # If 'TestCase:' is not found, return the original input string
        return test_string

test_string = "2023-04-27 15:30:45 - TestCase: login_successful"
result = solution(test_string)
print(result)

test_string = "2023-04-27 15:30:45 - test PASS"
result = solution(test_string)
print(result)

print('-' * 30, "lesson 4 - Tests", '-' * 30)

# Задача. Перевірка формату файлів у тестовому наборі
def check_file_format(file_list: list, extention: str):
    new_list = []

    for file in file_list:
        if file.endswith(extention):
            new_list.append(file)

    return new_list

# Тести
input_list = ["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"]
extenntion = ".txt"
expected_list = ["a.txt", "b.txt"]

input_list2 = ["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"]
extenntion2 = ".log"
expected_list2 = ["c.log", "e.log"]

input_list3 = ["a.txt", "b.txt", "c.log", "d.html", "e.log", ".diff"]
extenntion3 = ".json"
expected_list3 = []

print(check_file_format(input_list, extenntion))
print(check_file_format(input_list2, extenntion2))
print(check_file_format(input_list3, extenntion3))

print('-' * 30, "lesson 4 - Tests", '-' * 30)

list_num = [1, 2,3,4,5,6,7,8,9,10]

# even numbers
for num in list_num:
    if num % 2 == 0:
        print(num)

# odd numbers
for num in list_num:
    if num % 2 != 0:
        print(num)


returns_urls = ['www.simple.com/asd?a=b', 'www.simple.com/asd?', 'www.simple.com/xxxxxxx?a=b', 'www.s1imple.com/asd?a=b']
expected_start = 'www.simple.com'

index = 0
for url in returns_urls:
    res = url.startswith(expected_start)
    if not res:
        print(f'BAD CASE in position {index}: {url}')

    index += 1  # index = index + 1




