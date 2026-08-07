#Рефлексия
#Сканирование файлов. В общем решено верно, но при решении были допущены ошибки:
# - Не решено с помощью рекурсии
# - Использую конкотенацию вместо стандартных функций
#Удаление фалов
#В общем решено верно,но не использую первую функцию из задачи
#Напишите функцию, которая получает на вход два параметра: имя файла архива и расширение файла, сканирует текущий каталог в поисках файлов с подходящим расширением, и добавляет их в архив (исходно этот архив не существует).	
import os.path
from zipfile import ZipFile

def add_arch(arch_name, files_extension):
    if os.path.isfile(arch_name + '.zip'):
            with ZipFile(arch_name + '.zip', 'w') as testzip:
                pass
    for obj_os in os.listdir('./'):
        if os.path.isfile(obj_os):
            if os.path.splitext(obj_os)[1] == files_extension:

                with ZipFile(arch_name + '.zip', 'a') as testzip:
                    testzip.write(obj_os)

add_arch('my_zip', '.txt')