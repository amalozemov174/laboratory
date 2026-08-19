### Рефлексия по рпедыдущему занятию
Задание на ознакомление с трекером было выполнено
### Текущие задачи
### Установите линтер pylint. Проверьте линтером какой-нибудь свой код, несколько последних примеров, в отчёте в форме напишите 5-7 рекомендаций линтера -- что исправили

#### установка pylint
```bash
dnf install pylint
```
#### Для примера будем использовать задания на словари:

1. Напишите небольшую программу, которая добавляет в словарь 100 случайных пар (предварительно в массив например ключи записываем) целый ключ + значение строка, затем считывает по ключам все значения и выводит, и затем удаляет все пары.
2. Напишите функцию, которая получает список из 100 значений (сгенерируйте его заранее с числами в диапазоне от 1 до 10) и число N, и выдаёт список из тех значений в этом списке, которые повторяются не менее N раз. Используйте словарь для этого.
```python
import random

def first_work_with_dictionary():
    my_dict = {}
    list_key = []
    while len(list_key) < 100:
        list_key.append(random.randint(1, 1000))
    for i in range(len(list_key)):
        my_dict[i] = 'id' + str(list_key[i])
    for j in my_dict.keys():
        print(my_dict.get(j))    
    list_keys = list(my_dict.keys())
    for k in list_keys:
        del my_dict[k]    
		
first_work_with_dictionary()

import random

def get_repeat_numbers(list_numbers, count_number):
    my_dict = {}
    res_list = []
    for i in range(len(list_numbers)):
        if my_dict.get(list_numbers[i], 0) != 0:
            my_dict[list_numbers[i]] = my_dict.get(list_numbers[i]) + 1
        else:
            my_dict[list_numbers[i]] = 1
    for k in my_dict.keys():
        if my_dict.get(k) >= count_number:
            res_list.append(k)
    return res_list        
                     
my_list = []
for i in range(100):
    my_list.append(random.randint(1, 10))
print(get_repeat_numbers(my_list, 3)) 
```

запустим pylint
```bash
pylint dictionaries.py
```
получаем ответ:
```bash
[root@TDB-TXPGPOSTGRE2 ~]# pylint dictionaries.py
************* Module dictionaries
dictionaries.py:11:29: C0303: Trailing whitespace (trailing-whitespace)
dictionaries.py:14:22: C0303: Trailing whitespace (trailing-whitespace)
dictionaries.py:17:62: C0303: Trailing whitespace (trailing-whitespace)
dictionaries.py:18:72: C0303: Trailing whitespace (trailing-whitespace)
dictionaries.py:19:0: C0301: Line too long (115/100) (line-too-long)
dictionaries.py:33:19: C0303: Trailing whitespace (trailing-whitespace)
dictionaries.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
dictionaries.py:38:37: C0303: Trailing whitespace (trailing-whitespace)
dictionaries.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dictionaries.py:8:8: W0621: Redefining name 'i' from outer scope (line 36) (redefined-outer-name)
dictionaries.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
dictionaries.py:8:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
dictionaries.py:10:13: C0201: Consider iterating the dictionary directly instead of calling .keys() (consider-iterating-dictionary)
dictionaries.py:20:0: W0404: Reimport 'random' (imported line 1) (reimported)
dictionaries.py:20:0: C0413: Import "import random" should be placed at the top of the module (wrong-import-position)
dictionaries.py:25:8: W0621: Redefining name 'i' from outer scope (line 36) (redefined-outer-name)
dictionaries.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
dictionaries.py:25:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
dictionaries.py:30:13: C0201: Consider iterating the dictionary directly instead of calling .keys() (consider-iterating-dictionary)
dictionaries.py:35:0: C0103: Constant name "my_list" doesn't conform to UPPER_CASE naming style (invalid-name)

------------------------------------------------------------------
Your code has been rated at 3.33/10 (previous run: 3.33/10, +0.00)
```

Устраняем замечания по строкам:
```bash
dictionaries.py:17:62: C0303: Trailing whitespace (trailing-whitespace) 
```
удаляю лишние пробелы.
```bash
dictionaries.py:1:0: C0114: Missing module docstring (missing-module-docstring)
```
добавляю документационную строку -> """Модуль для работы со словарями и изучения их базовых методов"""
```bash
dictionaries.py:8:8: W0621: Redefining name 'i' from outer scope (line 36) (redefined-outer-name)
```
Выполнил переименование всех переменных в циклах на уникальные значения
```bash
dictionaries.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
```
Добавил описание функций
```bash
dictionaries.py:10:4: C0200: Consider using enumerate instead of iterating with range and len (consider-using-enumerate)
```
Использовал итерацию по значению вместо итерации по ид элемента в циклах for
```bash
dictionaries.py:12:13: C0201: Consider iterating the dictionary directly instead of calling .keys() (consider-iterating-dictionary)
```
убираю конструкцию .keys() при итерации по ключам словаря
```bash
dictionaries.py:33:0: C0103: Constant name "my_list" doesn't conform to UPPER_CASE naming style (invalid-name)
```
переименовал константу my_list в MY_LIST

Выполнил проверку снова
```bash
[root@TDB-TXPGPOSTGRE2 ~]# pylint dictionaries.py

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 3.33/10, +6.67)
```

Финальный код:
```python
"""Модуль для работы со словарями и изучения их базовых методов"""
import random

def first_work_with_dictionary():
    """Первая работа со словарем"""
    my_dict = {}
    list_key = []
    while len(list_key) < 100:
        list_key.append(random.randint(1, 1000))
    for i in list_key:
        my_dict[i] = 'id' + str(i)
    for j in my_dict:
        print(my_dict.get(j))
    list_keys = list(my_dict.keys())
    for k in list_keys:
        del my_dict[k]

def get_repeat_numbers(list_numbers, count_number):
    """Функция вывода количесва повторяющихся значений из списка"""
    my_dict = {}
    res_list = []
    for num in list_numbers:
        if num in my_dict:
            my_dict[num] = my_dict.get(num) + 1
        else:
            my_dict[num] = 1
    for my_k in my_dict:
        if my_dict.get(my_k) >= count_number:
            res_list.append(my_k)
    return res_list

first_work_with_dictionary()
MY_LIST = []
for el in range(100):
    MY_LIST.append(random.randint(1, 10))
print(get_repeat_numbers(MY_LIST, 3))
```