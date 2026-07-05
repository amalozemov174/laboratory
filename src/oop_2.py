#Рефлексия
# Задание в общем выполнил корректно были продуманы иерархии классов
# Реализованы конструкторы и уникальные методы для каждого конкретного класса
##########################################
#4.1. Реализуйте композицию для двух иерархий классов из предыдущего занятия. 
# Напишите код для работы с объектами соответствующих классов, из которого наглядно понятна идея композиции.

class ElectronicDevice:

    def __init__(self, cpu, ram, dimensions):
        self.__cpu = cpu
        self.__ram = ram
        self.__dimensions = dimensions
        
    def start_work(self):
        print(f'запуск устройства {self.__cpu.use()} и {self.__ram.use()}')
    
class ElectronicComponent:

    def use(self):
        return 0
    
    
class Cpu(ElectronicComponent):
    def __init__(self, frequency, cores_num, cache):
        self.frequency = frequency
        self.cores_num = cores_num
        self.cache = cache
        
    def use(self):
        return f'Вычисления математических операций с частотой {self.frequency}'    
        
class Ram(ElectronicComponent):
    def __init__(self, frequency, size):
        self.frequency = frequency
        self.size = size

    def use(self):
        return f'Сохранение данных в RAM {self.size}'        

class Dimensions:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        
class Camera(ElectronicComponent):
    def __init__(self, resolution):
        self.resolution = resolution
            
    def use(self):
        return f'Фотография с разрешением {self.resolution}'        
        

class Freezer(ElectronicComponent):        
    def __init__(self, frezer_model):
        self.frezer_model = frezer_model
        
    def use(self):
        return f'охлаждение с помощью холодильника {self.frezer_model}'            

class Mobilephone(ElectronicDevice):

    def __init__(self, cpu, ram, dimensions, rington, camera):
        super().__init__(cpu, ram, dimensions)
        self.__rington = rington
        self.__camera = camera
		
    def ring(self):
        print(f'Проиграть мелодию {self.__rington}') 
		
    def take_photo(self):
        print(f'Фотография с разрешением {self.__camera.use()}') 

class Fridge(ElectronicDevice):

    def __init__(self, cpu, ram, dimensions, frezer):
        super().__init__(cpu, ram, dimensions)
        self.__frezer = frezer
        self.__frezee = -10
        self.__is_door_open = False
				
    def make_frezee(self, frezee):
        self.__frezee -= frezee
		
    def open_door(self):
        if self.__is_door_open:
            self.__is_door_open = False
        else:
            self.__is_door_open = True
            			
    def start_frezee(self):
        print(f'{self.__frezer.use()}')               

print('Мобильный телефон')
cpu = Cpu("3.2 GHz", 8, "4 MB")
ram = Ram("4200 MHz", "12 GB")
dimensions = Dimensions(180, 160)
rington = "123.mp3"
camera = Camera("50 MP")
phone = Mobilephone(cpu, ram, dimensions, rington, camera)
phone.start_work()
phone.take_photo()
phone.ring()
print('Холодильник')
cpu = Cpu("0.2 GHz", 8, "1 MB")
ram = Ram("200 MHz", "1 GB")
dimensions = Dimensions(12180, 5160)
freezer = Freezer('модель 1') 
fridge = Fridge(cpu, ram, dimensions, freezer)
fridge.start_frezee()


# 4.2. Расскажите своими словами, как вы поняли пример с двумя видами полиморфизма.

#Первый метод полиморфизма работает с типами и подбирает метод в зависимости от используемого типа или выбирает метод в зависимости от количесвта переменных поданых на вход метода
#Второй метод используется реализация метода не зависит от типа переданного объекта

# 4.3. Напишите функцию, которая получает на вход список list[Animal] из этого примера, очищает его, и затем заполняет 500 объектами, где будут случайно перемешаны 500 объектов двух дочерних классов.
# Не забывайте, что объекты обычным присваиванием не копируются.
# Получите с её помощью результат, и в цикле, не зная где какой объект, вызывайте foo().
# Почему получился такой вывод?
import random
class Animal:
    def foo(self):
        pass

class Cat(Animal):
    def foo(self):
        print("Кошка мурлычет")

class Bird(Animal):
    def foo(self):
        print("Птица поет")

def do_something_with_animal(animal: Animal):
    animal.foo()
    
def do_something_with_list_animal(animals: list[Animal]):
    animals_size = 500
    for i in range(len(animals) - 1, -1, -1):
        animals.pop(i)
    for i in range(animals_size):
            tmp_rnd = random.randint(1,2)
            if tmp_rnd == 1:
                animals.append(Cat())        
            else:
                animals.append(Bird())

#cat = Cat()
#bird = Bird()

#do_something_with_animal(cat)
#do_something_with_animal(bird)

animals = [Cat(), Bird()]                
do_something_with_list_animal(animals)
for i in range(len(animals)):
    animals[i].foo()
# Для каждого объекта из списка будет вызван метод класса согласно полиморфизму подтипов. Поэтому мы видим вывод методов - текст Птица поет или Кошка мурлычет
# А согласно параметрическоиу полиморфизму цикл for будет одинаково вызыван для все элементов из списка animals вне зависимости от их типа 