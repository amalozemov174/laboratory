# Рефлексия
# В целом решено верно, но в моем решении нее хватает базовой логики игры, 
# т.е. методы просто присваиваю/возвращают значение
#########################################################################
#5.1
class Player:

    def __init__(self, player_name, player_age, player_position, player_team_name, player_speed, player_power_goal):
        self.__name = player_name
        self.__age = player_age
        self.__position = player_position
        self.__team_name = player_team_name
        self.__player_speed = player_speed
        self.__power_goal = player_power_goal

    def get_name(self):
        return self.__name

    def change_name(self, new_name):
        self.__name = new_name
		
    def get_age(self):
        return self.__age

    def become_older(self):
        self.__age += 1
		
    def get_position(self):
        return self.__position
		
    def change_position(self, new_position):
        self.__position = new_position

    def run(self, increase_speed):
        self.__player_speed += increase_speed
		
    def get_speed(self):
        return self.__player_speed
		
    def train_kick(self, add_kick_power):
        self.__power_goal += add_kick_power
		
    def kick(self):
        return self.__power_goal
		
    def change_team(self, new_team_name):
        self.__team_name = new_team_name
		
    def get_team(self):
        return self.__team_name


class Team:

    def __init__(self, team_name, stadium_name, player_uniform):
        self.__team_name = team_name
        self.__stadium_name = stadium_name
        self.__player_uniform = player_uniform
        self.__players = []

    def change_team_name(self, new_team_name):
        self.__team_name = new_team_name
		
    def get_team(self):
        return self.__team_name

    def add_player(self, player):
        self.__players.append(player)
		
    def get_players(self):
        return self.__players

    def count_players(self):
        return len(self.__players)

    def change_stadium_name(self, new_stadium_name):
        self.__stadium_name = new_stadium_name

    def show_stadium(self):
        print("Название стадиона:", self.__stadium_name)    
		
    def change_player_uniform(self, new_player_uniform):
        self.__player_uniform = new_player_uniform
		
    def get_player_uniform(self):
        return self.__player_uniform
		
		
#5.2. Постройте две небольшие и косвенно логически связанные иерархии классов в вашей программе (например, Животное - Кот/Собака, и Переноска животных - Сумка для котика/Чемодан для собаки).
#Не выдумывайте никакие абстрактные сущности, только запутаетесь. Возьмите простые физические вещи, например, автомобиль и двигатель, тарелка и еда, кошелёк и деньги и т. п..
#У родительского класса в каждой иерархии должно быть не менее двух наследников.
#В каждом дочернем классе должно быть не менее двух оригинальных методов, характеризующих уникальность этих классов, их отличие от родительского.		

#1ая иерархия Животное - Кот/Кит

class Animal:

    def __init__(self, age, body_color, weight, height):
        self.__age = age
        self.__body_color = body_color
        self.__weight = weight
        self.__height = height
		
class Cat(Animal):    
    
    def __init__(self, age,body_color,weight,height, name):
        super().__init__(age,body_color,weight,height)
        self.__name = name
        self.__jump_height = 10
        self.__fq = 100
    
    def purr(self, freq):
        return self.__fq

    def jump(self, jump_height):
        self.__jump_height += jump_height
		
class Whale(Animal):    
    
    def __init__(self, age,body_color,weight,height):
        super().__init__(age,body_color,weight,height)      
        self.__deep = 100
        self.__blow = 10
		
    def dive(self):
        return self.__deep

    def blow_water(self):
        return self.__blow
		
		
#2ая иерархия Электронный девайс - мобидьный телефон/Холодидьник
class ElectronicDevice:

    def __init__(self, cpu, ram, weight, height):
        self.__cpu = cpu
        self.__ram = ram
        self.__weight = weight
        self.__height = height
		
class Mobilephone(ElectronicDevice):

    def __init__(self, cpu, ram, weight, height, rington, camera):
        super().__init__(cpu, ram, weight, height)
        self.__rington = rington
        self.__camera = camera
		
    def ring(self):
        return self.__rington
		
    def take_photo(self):
        return self.__camera

class Fridge (ElectronicDevice):

    def __init__(self, cpu, ram, weight, height):
        super().__init__(cpu, ram, weight, height)
        self.__frezee = -10
        self.__is_door_open = False
				
    def make_frezee(self, frezee):
        self.__frezee -= frezee
		
    def open_door(self):
        if self.__is_door_open:
            self.__is_door_open = False
        else:
            self.__is_door_open = True			