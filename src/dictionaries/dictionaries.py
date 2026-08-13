#Рефлексия
#Решено неверно:
# - объединил два задания в одну функцию
# - первое задание в общем решено верно
#Второе задание решено частично, прямоугольник с надписью рисуется по центру,
# но размер шрифта, стиль шрифта, выделение шрифта не подобрано
#########################################################################
# 1. Напишите небольшую программу, которая добавляет в словарь 
# 100 случайных пар (предварительно в массив например ключи записываем)
# целый ключ + значение строка,
# затем считывает по ключам все значения и выводит, и затем удаляет все пары.
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
# 2. Напишите функцию, которая получает список из 100 значений 
# (сгенерируйте его заранее с числами в диапазоне от 1 до 10) и число N, 
# и выдаёт список из тех значений в этом списке, которые повторяются не менее N раз. Используйте словарь для этого.
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