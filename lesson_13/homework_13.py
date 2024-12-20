
from pathlib import Path
import logging

'''
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
результат для невалідного файлу виведіть через логер на рівні error у файл json__<your_second_name>.log
'''
#parent_dir = Path('/Users/Anton/python/python_learning/py_30_Days/lesson_13')
current_dir = Path.cwd()
extension = '.json'
files_with_json_extencion = [ f for f in current_dir.iterdir() if f.suffix == extension]

for file in files_with_json_extencion:
    print(file)

with open('/Users/Anton/python/python_learning/py_30_Days/lesson_13/json__<your_second_name>.log', 'w') as file2:
    file2.write('not valid json')

def log_json():

    log_message = "Login json"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='json__<Kolomiiets>.log',
        level=logging.ERROR,
        format='%(asctime)s - %(message)s - %(levelname)s',
        force=True
        )
    logger = logging.getLogger("log_json")




