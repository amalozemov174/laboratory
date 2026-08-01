### Рефлексия по предыдущему занятию
#### Тестирование случайных значений 
В общем верное, но метод сравения массивов был выбран,
вероятно, неправильно, т.к. сравниваются два массива в assertEquals, а не по элемнтно,
хотя сказано, что если передать два массива он сравнит их поэлементно
#### Регрессия
В общем решено верно, но решение более топорное с прямым сравниванием массивов
#### Странные значения
В обще решено верно, с бесконечными значеняими не додумался
#### Пустой массив
В общем решено верно, но в мое решение не помешало бы добаить, как в эталонном решение массив с 1 нулевым элементом
### Текущие задачи

### 3.1. Программно создайте 10 файлов с именами 1.txt, 2.txt, ..., 10.txt, и в каждый запишите три случайных числа, каждое с новой строки.

## Код программы на python
```python
def createFiles():
    for i in range (1, 11):
        with open(f'{i}.txt', 'wt') as file:
            for i in range (3):
                file.write(str(randint(-25,+25)) + "\n")
```
### 3.2. Напишите функцию, которая получает на вход два случайных числа от 1 до 10 и путь к файлам, по этим числам открывает два соответствующих файла из задания выше, и возвращает сумму шести чисел (содержимое обоих файлов). Если содержимое любого файла неполно или испорчено, возвращайте информацию об ошибке (подумайте, как лучше организовать такую функцию).
```python
def readFiles():
    res = 0
    for i in range (2):
        try:
            with open(f'{randint(1,10)}.txt', 'rt') as file_read:
                for s in file_read:
                    try:
                        tmp = int(s.rstrip())
                        res += tmp
                    except ValueError:
                        print(f'Ошибка, невозможно значение {s.rstrip()}, не число. Используем следующее число')
        except:
            return None                 
    return res
```
### 3.3. Напишите программу, которая считывает из текстового файла строки, каждая из которых задаёт содержимое объекта некоторого класса. 
```python
from random import randint
import random
class Cat:
    
    def __init__(self, cat_name, cat_weight, cat_purr):
        self.__name = cat_name
        self.__weight = cat_weight
        self.__purr = cat_purr
    
    def getCatName(self):
        return self.__name
    
    def getCatWeight(self):
            return self.__weight
        
    def getCatPurr(self):
            return self.__purr

def makeCats():
    cats = []
    try:
        with open('cats.txt', 'rt') as file_cats_read:        
            for cat_str in file_cats_read:
                cat_params = cat_str.rstrip().split()
                if len(cat_params) < 3:
                    print('Ошибка при создании Кота не хватает параметров')
                    continue 
                cat_name = cat_params[0]
                if len(list(cat_name)) <= 0 or len(list(cat_name)) >= 30:
                    print(f'Ошибка при создании Кота. Некорректное имя {cat_name}')
                    continue
                try:
                    cat_weigth = float(cat_params[1])
                except:
                    print(f'Ошибка при создании Кота. Некорректный вес {cat_weigth}')
                    continue
                if cat_weigth <= 0 or cat_weigth >= 30:
                    print(f'Ошибка при создании Кота. Некорректный вес {cat_weigth}')
                    continue
                try:
                    cat_purr = int(cat_params[2])
                except:
                    print(f'Ошибка при создании Кота. Некорректная частота мурлыканья {cat_purr}')
                    continue
                if cat_purr <= 0 or cat_purr >= 10000:
                    print(f'Ошибка при создании Кота. Некорректная частота мурлыканья {cat_purr}')
                    continue       
                cat_obj = Cat(cat_params[0], cat_weigth, cat_purr)           
                cats.append(cat_obj)
    except:
        return cats                    
    return cats            
```
Для всех задач были написаны тестове кейсы
- files_test.py
- read_files.py
- cat_test.py