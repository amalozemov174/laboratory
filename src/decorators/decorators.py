#Рефлексия
#На прошлом занятии ознакомился и применил pylint
##################################
#7. Задания.

#7.1. Напишите два оригинальных декоратора.

import logging
import time
import functools

def log_decorator(func):
    """Декоратор, который выводит выполняет логгирование через logging."""
    def wrapper(*args, **kwargs):
        logging.basicConfig(filename='debug.log', level=logging.INFO)
        logger = logging.getLogger(__name__)
        logger.info(f"Вызов функции {func.__name__} с аргументами: {args} и {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Функция {func.__name__} завершилась с результатом: {result}")
        return result
    return wrapper

def timer(func):
    """Декоратор, который выводит время выполнения функции."""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Функция {func.__name__!r} выполнилась за {run_time:.4f} с.")
        return value
    return wrapper_timer


@log_decorator
@timer
def sum(first,second):
    return first + second

@log_decorator
@timer	
def diff(first,second):
    return first - second

@log_decorator
@timer	
def multiplication(first,second):
    return first * second
	
# 7.2. Добавьте в ваши классы из первых занятий, где мы проходили геттеры и сеттеры, соответствующие декораторы.
   
class Player:

    def __init__(self, name, age, position, team_name, speed, power_goal):
        self._name = name
        self._age = age
        self._position = position
        self._team_name = team_name
        self._speed = speed
        self._power_goal = power_goal
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
		
    @property	
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
	
    @property	
    def position(self):
        return self._position
		
    @position.setter
    def position(self, position):
        self._position = position

    @property	
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed += speed
	
    @property
    def power_goal(self):
        return self._power_goal
 
    @power_goal.setter
    def power_goal(self, power_goal):
        self._power_goal += power_goal
		
    @property
    def team_name(self):
        return self._team_name
  
    @team_name.setter  
    def team_name(self, team_name):
        self._team_name = team_name


class Team:

    def __init__(self, team_name, stadium_name, player_uniform):
        self.__team_name = team_name
        self.__stadium_name = stadium_name
        self.__player_uniform = player_uniform
        self.__players = []

    @property
    def team_name(self):
        return self.__team_name

    @team_name.setter
    def team_name(self, team_name):
        self.__team_name = team_name

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, players):
        self.__players = players
		
    def count_players(self):
        return len(self.__players)

    @property
    def stadium_name(self):
        return self.__stadium_name

    @stadium_name.setter
    def stadium_name(self, stadium_name):
        self.__stadium_name = stadium_name    
	
    @property
    def player_uniform(self):
        return self.__player_uniform   
  
    @player_uniform.setter
    def player_uniform(self, player_uniform):
        self.__player_uniform = player_uniform


# 7.3. Своими словами расскажите, как вы поняли, в чём разница между статическим методом и методом класса.
#Статический метод принадлежит класуу и вызывается при обращении к классу может использоваться как дополнительная функция. а метод класса это метод, который имеет доступ к переменным и функциям класса

# 7.4. Добавьте в какой-нибудь свой класс поддержку инварианта.
from functools import wraps

def invariant(predicate):
    def invariant_decorator(method):
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            result = method(self, *args, **kwargs)
            assert predicate(self), f"Invariant condition failed {method.__name__}"
            return result
        return wrapper
    return invariant_decorator

class Player:

    def __init__(self, name, age, position, team_name, speed, power_goal):
        self._name = name
        self._age = age
        self._position = position
        self._team_name = team_name
        self._speed = speed
        self._power_goal = power_goal
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
		
    @property	
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
	
    @property	
    def position(self):
        return self._position
		
    @position.setter
    def position(self, position):
        self._position = position

    @property	
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed += speed
	
    @property
    def power_goal(self):
        return self._power_goal
 
    @power_goal.setter
    def power_goal(self, power_goal):
        self._power_goal += power_goal
		
    @property
    def team_name(self):
        return self._team_name
  
    @team_name.setter  
    def team_name(self, team_name):
        self._team_name = team_name
        
    @invariant(lambda self: self._speed >= 0)    
    def decrese_speed(self, value):
        self._speed -= value     

# 7.5. Добавьте в свой код assert-ы по пунктам 5.1-5.7.

#5.1

def sum(first, second):
    assert isinstance(first, int), "Value must be an integer"
    assert isinstance(second, int), "Value must be an integer"
    return first + second

#5.2

def count_words(s):
    sl = list(s)
    count = 0
    is_word = False
    for i in range(len(sl)):
        if sl[i] != ' ':
            if is_word != True:
                count += 1
                is_word = True
        else:
            is_word = False
    assert count >= 0, "Result should be more or equal zero"        
    return count

#5.3

def decrese_speed(self, speed):
    assert 0 <= speed <= 50, "Age must be between 0 and 50"
    self._speed -= speed

#5.4
        
def count_words(s):
    assert s is not None, "String cannot be None"
    assert len(s) > 0, "String cannot be empty"
    sl = list(s)
    count = 0
    is_word = False
    for i in range(len(sl)):
        if sl[i] != ' ':
            if is_word != True:
                count += 1
                is_word = True
        else:
            is_word = False
    return count        

#5.5

def calculate_age(birth_year):
    current_year = 2026
    assert birth_year <= current_year, "birth_year can't be more then current_year"
    return current_year - birth_year

#5.6    
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
    assert animals is not None and isinstance(animals, list), "'animals' must be initialized and to be as list"
    animals_size = 500
    for i in range(len(animals) - 1, -1, -1):
        animals.pop(i)
    for i in range(animals_size):
            tmp_rnd = random.randint(1,2)
            if tmp_rnd == 1:
                animals.append(Cat())        
            else:
                animals.append(Bird())    
    
#5.7

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
    assert isinstance(animal, Animal), "Object has to be an heir of class Animal"
    animal.foo()
    
def do_something_with_list_animal(animals: list[Animal]):
    assert animals is not None and isinstance(animals, list), "'animals' must be initialized and to be as list"
    animals_size = 500
    for i in range(len(animals) - 1, -1, -1):
        animals.pop(i)
    for i in range(animals_size):
            tmp_rnd = random.randint(1,2)
            if tmp_rnd == 1:
                animals.append(Cat())        
            else:
                animals.append(Bird())    

# 7.6. Напишите своими словами, как вы поняли код с ad hoc полиморфизмом.
# ad hoc полиморфизм предлагает вариант перегрузки методов с различными типами данных, т.е. для каждого типа своя логика обработки