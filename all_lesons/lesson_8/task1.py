"""
Напишіть програму, яка відкриває файл "data.txt" для читання та читає числа з файлу.
Підрахуйте суму всіх чисел, прочитаних з файлу.
Забезпечте обробку можливих виключень:
Обробіть виняток, якщо файл не знайдено. (FileNotFoundError). Функція повинна вертати строку “File not found”
Обробіть виняток, якщо зміст файлу містить нечислові значення. (ValueError).
 Функція повинна вертати строку “Invalid data in the file”
Виведіть суму чисел, якщо операція пройшла успішно. В іншому випадку виведіть інформацію про виняток, який виник.

Закрийте файл навіть у випадку виняткової ситуації.
"""
def calculate_sum_from_file(filename):

    try:
        with open(f'{filename}', 'r') as f:
            content = f.read().split()

        return sum([int(i) for i in content])

    except FileNotFoundError:
        return "The file is not found!"
    except ValueError:
        return "Invalid data in the file"



print(calculate_sum_from_file('data.txt'))

for index, item in enumerate([10,20,30]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Ukraine']

nordic_countries = [k for k in countries[:5]]
print('nordic_countries:', *nordic_countries)

es_countries = [k for k in countries[5:6]]
print('es_countries:', *es_countries)

ua = [k for k in countries[-1:]]
print('UA:', *ua)




