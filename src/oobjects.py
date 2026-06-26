# 1.1. 
# 1ая программа база данных
#     База данных - содержит, схему, пользователя
#     Схема - содержит таблицы, пользователей, функции, очереди
#     Таблица - содержит строки
#     Строка - содержит значения полей
#     Тип данных - Содержит различные типы данных
#     Пользователь - содержит логин, пароль, права доступа
#     Функция - хранит имя функции, параметры и её код
#     Очередь - хранит список запросов и их статус
# 2ая программа Интернет магазин WB
#     Товар - название, цена, тип товара
#     Корзина - список товаров, общая суммма
#     Покупатель - имя, адрес, телефон
#     Заказ - список товаров, общая цена, статус доставки
#     Категория товара - тип товара
# 3я программа игра pro evolution soccer
#     Команда - спсиок игроков, тренер, стадион на которм играет команада
#     Игрок - имя, возраст, позиция, команда, скорость, сила удара
#     Тренер - имя, возраст, комнда, трофеи, зарплата, стиль игры
#     Стадион - название, вместимость, тип поля

# 1.2
# Тема игра pro evolution soccer
# Класс Игрок: имя, возраст, позиция, команда, скорость, сила удара
# Класс Тренер: имя, возраст, комнда, трофеи, зарплата, стиль игры
# Класс Команда: спсиок игроков, тренер, стадион на которм играет команада, название, форма
class Player:
    name = 'Имя'
    age = 0
    position = 'Позиция'
    team_name = 'Имя команды'
    speed = 100
    power_goal = 0
    
class Manager:
    name = 'Имя'
    age = 0
    team_name = 'Имя команды'
    trophies = []
    salary = 0
    game_style = ''

class Team:
    players = []
    manager = ''
    stadium_name = ''
    team_name = ''
    player_uniform = ''
    
player1 = Player()
player1.name = 'Петя'
player1.age = 20
player1.position = 'Нападающий'
player1.team_name = 'Зенит'
player1.speed = 10
player1.power_goal = 10
player2 = Player()
player2.name = 'Дима'
player2.age = 30
player2.position = 'Полузащитник'
player2.team_name = 'ЦСКА'
player2.speed = 5
player2.power_goal = 5
player3 = Player()
player3.name = 'Вова'
player3.age = 40
player3.position = 'Вратарь'
player3.team_name = 'Спартак'
player3.speed = 1
player3.power_goal = 1
manager1 = Manager()
manager1.name = 'Женя'
manager1.age = 50
manager1.team_name = 'Зенит'
manager1.trophies = ['Кубок России']
manager1.salary = 100
manager1.game_style = 'Нападение'
manager2 = Manager()
manager2.name = 'Иван'
manager2.age = 60
manager2.team_name = 'Спартак'
manager2.trophies = ['Чемпионат России']
manager2.salary = 200
manager2.game_style = 'Защита'
manager3 = Manager()
manager3.name = 'Олег'
manager3.age = 70
manager3.team_name = 'ЦСКА'
manager3.trophies = ['Чемпионат 2-ой Лиги']
manager3.salary = 10
manager3.game_style = 'Защита'
team1 = Team()
team1.players = [player1.name]
team1.manager = manager1.name
team1.stadium_name = 'Зенит арена'
team1.team_name = 'Зенит'
team1.player_uniform = 'Бирюзовый'
team2 = Team()
team2.players = [player2.name]
team2.manager = manager3.name
team2.stadium_name = 'ЦСКА арена'
team2.team_name = 'ЦСКА'
team2.player_uniform = 'Красно-Синий'
team3 = Team()
team3.players = [player3.name]
team3.manager = manager2.name
team3.stadium_name = 'Спартак арена'
team3.team_name = 'Спартак'
team3.player_uniform = 'Красно-Белый'
print(f'Игрок: Имя:{player3.name}, Возраст:{player3.age}, Позиция:{player3.position}, Имя команды:{player3.team_name}, Скорость:{player3.speed}, Мощность удара:{player3.power_goal}')
print(f'Игрок: Имя:{player2.name}, Возраст:{player2.age}, Позиция:{player2.position}, Имя команды:{player2.team_name}, Скорость:{player2.speed}, Мощность удара:{player2.power_goal}')
print(f'Игрок: Имя:{player1.name}, Возраст:{player1.age}, Позиция:{player1.position}, Имя команды:{player1.team_name}, Скорость:{player1.speed}, Мощность удара:{player1.power_goal}')
print(f'Тренер: Имя:{manager1.name}, Возраст:{manager1.age}, Трофеи:{manager1.trophies}, Зарплата:{manager1.salary}, Стиль игры:{manager1.game_style}')
print(f'Тренер: Имя:{manager2.name}, Возраст:{manager2.age}, Трофеи:{manager2.trophies}, Зарплата:{manager2.salary}, Стиль игры:{manager2.game_style}')
print(f'Тренер: Имя:{manager3.name}, Возраст:{manager3.age}, Трофеи:{manager3.trophies}, Зарплата:{manager3.salary}, Стиль игры:{manager3.game_style}')
print(f'Команда: Название команды:{team1.team_name}, Имена игроков:{team1.players}, Название стадиона:{team1.stadium_name}, Цвет формы:{team1.player_uniform}, Имя тренера:{team1.manager}')
print(f'Команда: Название команды:{team2.team_name}, Имена игроков:{team2.players}, Название стадиона:{team2.stadium_name}, Цвет формы:{team2.player_uniform}, Имя тренера:{team2.manager}')
print(f'Команда: Название команды:{team3.team_name}, Имена игроков:{team3.players}, Название стадиона:{team3.stadium_name}, Цвет формы:{team3.player_uniform}, Имя тренера:{team3.manager}')
#1.3.
player4 = player3
#изменяем параметр age на 41
player4.age = 41
#интуитивно кажется, что был изменен параметр у объекта player4, но на самом деле т.к. plaer4 ссылается на player3
#парамет age поменяется и у player4 и у player3
print(player4.age)
print(player3.age)