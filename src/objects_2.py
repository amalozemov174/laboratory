#Рефлексия
#1.2 В общем мое решение верное. Но думаю что мои классы немного абстрактные
#######################################
# Дополните два класса, которые вы спроектировали в предыдущем задании, методами, подходящими для логики работы с ними. 
# В каждом классе должно быть не менее трёх методов. Добавьте в каждый класс конструктор.
# Если предыдущий вариант оказался не очень удачным (так как вы создавали классы, исходя из списка их атрибутов), придумайте новые классы.
# Создайте несколько объектов этих классов, повызывайте их методы, выведите вычисляемые с помощью методов значения на экран.

class Player:

    def __init__(self, player_name, player_age, player_position, player_team_name, player_speed, player_power_goal):
        self.name = player_name
        self.age = player_age
        self.position = player_position
        self.team_name = player_team_name
        self.player_speed = player_speed
        self.power_goal = player_power_goal

    def run(self, new_player_speed):
        self.player_speed = new_player_speed
		
    def kick(self, new_power_goal):
        self.power_goal = new_power_goal	
		
    def change_team(self, new_team_name):
        self.team_name = new_team_name


class Team:

    def __init__(self, team_name, stadium_name, player_uniform):
        self.team_name = team_name
        self.stadium_name = stadium_name
        self.player_uniform = player_uniform
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def count_players(self):
        return len(self.players)

    def show_stadium(self):
        print("Название стадиона:", self.stadium_name)    

player1 = Player("Дзюба", 39, "Нападающий", "Зенит", 32, 95)
team1 = Team("Спартак", "Спартак Арена", "Красная")
player1.run(35)
player1.kick(99)
player1.change_team("Спартак")
print("Новая скорость:", player1.player_speed)
print("Новая сила удара:", player1.power_goal)
print("Новая команда:", player1.team_name)
team1.add_player(player1)
team1.show_stadium()
print("Всего игроков в команде:", team1.count_players())