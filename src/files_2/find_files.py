import os.path
import shutil

#Рефлексия
#3.1 В общем решено верно
#3.2 Думаю, что задание решено мной с ошибкой, т.к. битые числа игнорируются. Информация об ошибке текстовая, такую тяжело обработать
#3.3 Идея для решения у меня, выглядит верно, но переусложнил код с проверками на корректность создания объекта 
###############################

def get_files_list(path, file_extension, flag):
    res_files = []
    res_catalogs = []
    for obj_os in os.listdir(path):
        if os.path.isfile(path + obj_os):
            if os.path.splitext(obj_os)[1] == file_extension:
                res_files.append(obj_os)
        else:
            if flag:
                for obj_sub_catalog in os.listdir(path + obj_os + '/'):
                   if os.path.isfile(path + obj_os + '/' + obj_sub_catalog):
                       if os.path.splitext(obj_sub_catalog)[1] == file_extension:
                           res_files.append(obj_sub_catalog)
                   else:
                       res_catalogs.append(obj_sub_catalog)
            res_catalogs.append(obj_os)
    res_list = [res_files, res_catalogs]
    return res_list

def del_directory(path):
    for obj_os in os.listdir(path):
        if os.path.isfile(path + obj_os):
            continue
        else:
            return False
    for obj_os in os.listdir(path):
        os.remove(path + obj_os)
    os.rmdir(path)
    return True
