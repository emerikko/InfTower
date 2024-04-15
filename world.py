import player as pl
import cell as cl
from random import randint, random, choice

# Движок игры

class World:
    # Всякий мусор
    world = []
    height: int
    width: int
    _player = pl.Player()
    pl_x = 1
    pl_y = 1

    def __init__(self, x: int, y: int):
        self._player = pl.Player()  # Создаю игрока
        self.width = x  # Обозначаю x за собственную ширину мира
        self.height = y  # Обозначаю y за собственную высоту мира
        for i in range(y):  # Создаю y-вое количество листов
            self.world.append([])
            for _ in range(x):  # В каждую строку добавляю x-вое количество клеток
                self.world[i].append(cl.Cell())
        # В случайной точке, не на границе карты ставлю игрока
        self.pl_x = randint(1, x - 2)
        self.pl_y = randint(1, y - 2)

        for m in range(x):  # На краях, по стороне y ставлю стенки
            self.world[0][m].set_is_blocked(True)
            self.world[y - 1][m].set_is_blocked(True)
        for n in range(y):  # На краях, по стороне y ставлю стенки
            self.world[n][0].set_is_blocked(True)
            self.world[n][x - 1].set_is_blocked(True)
        self.update_v()  # Обновляю клетки, увиденные игроком

    def get_cell(self, y: int, x: int) -> cl.Cell:  # Возвращаем клетку по координатам
        return self.world[y][x]

    def pretty_print(self):  # Красивая отрисовка без тумана войны
        for i in range(self.width):  # Пробегаемся по y
            line = ''
            for j in range(self.height):  # Пробегаемся по x
                if j == self.pl_y and i == self.pl_x:
                    line += 'Pl'  # Записываем игрока в строку
                # Записываем восклицательный знак в строку, если на клетке указано, что там монстряк
                elif self.world[j][i].is_dangerous():
                    line += '! '
                elif self.world[j][i].is_blocked():
                    line += '# '  # Записываем стену в строку
                else:
                    line += '  '  # Записываем свободную клетку в строку, если игрок её видел
            print(line)  # Выводим записанную строку

    def pretty_print_v(self):  # Красивая отрисовка с туманом войны
        for i in range(self.width):  # Пробегаемся по y
            line = ''
            for j in range(self.height):  # Пробегаемся по x
                if j == self.pl_y and i == self.pl_x:
                    line += 'Pl'  # Записываем игрока в строку
                # Записываем восклицательный знак в строку, если на клетке указано, что там монстряк
                elif self.world[j][i].is_dangerous():
                    line += '! '
                elif self.world[j][i].is_blocked() and self.world[j][i].is_visited():
                    line += '# '  # Записываем стену, если мы её видели в строку
                elif self.world[j][i].is_visited():
                    line += '  '  # Записываем свободную клетку в строку, если игрок её видел
                else:
                    line += '? '  # Записываем вопросительный знак в строку, если игрок там ничего не видел
            print(line)  # Выводим записанную строку

    def update_v(self):  # Функция, обновляющая то, были ли замечены клетки
        # Обнаруживаю клетку под игроком и соседние
        self.world[self.pl_y][self.pl_x].set_is_visited(True)
        self.world[self.pl_y + 1][self.pl_x].set_is_visited(True)
        self.world[self.pl_y - 1][self.pl_x].set_is_visited(True)
        self.world[self.pl_y][self.pl_x + 1].set_is_visited(True)
        self.world[self.pl_y][self.pl_x - 1].set_is_visited(True)

        # Делаю так, что если у углов карты соседние клетки замечены - то они тоже становятся замеченными. Так красивее
        if self.world[0][1].is_visited() and self.world[1][0].is_visited():
            self.world[0][0].set_is_visited(True)
        if self.world[self.height - 1][1].is_visited() and self.world[self.height - 2][0].is_visited():
            self.world[self.height - 1][0].set_is_visited(True)
        if self.world[0][self.width - 2].is_visited() and self.world[1][self.width - 1].is_visited():
            self.world[0][self.width - 1].set_is_visited(True)
        if self.world[self.height - 2][self.width - 1].is_visited() and self.world[self.height - 1][self.width - 2]\
                .is_visited():
            self.world[self.height - 1][self.width - 1].set_is_visited(True)

    @property
    def player(self):  # Возврат игрока
        return self._player

    def checker(self, y: int, x: int):  # Функция, проверяющая, может ли оказаться игрок на запрошенных координатах
        if not self.get_cell(y, x).is_blocked():  # Если на какой-то клетке нет стены - возвращаю True
            # В будущем здесь будет больше проверок
            return True
        return False  # Если на какой-то клетке есть стена - возвращаю False

    def action(self, act: str, stage: int, player=_player):  # Функция, выполняющая действия, запрошенные игроком
        attributes = self.get_cell(self.pl_y, self.pl_x).items.get_att()  # Получаю свойства клетки с игроком
        possible_acts = self.get_possible_actions()  # Получаю список возможных действий
        for i in range(100):  # Чтобы был эффект, что карта обновляется
            print("")
        if "no_away" not in attributes:  # Смотрю, может ли двигаться пользователь
            match str(act):  # Смотрю действия, выбранные пользователем, если он может двигаться
                case 'N':  # Смотрю, что выбрал пользователь
                    if 'N' in possible_acts:  # Проверяю, можем ли мы сделать это действие
                        self.pl_x -= 1  # Двигаю игрока
                        self.update_v()  # Обновляю карту
                        self.pretty_print_v()  # Вывожу изученную карту
                        return
                case 'E':  # Смотрю, что выбрал пользователь
                    if 'E' in possible_acts:  # Проверяю, можем ли мы сделать это действие
                        self.pl_y += 1  # Двигаю игрока
                        self.update_v()  # Обновляю карту
                        self.pretty_print_v()  # Вывожу изученную карту
                        return
                case 'S':  # Смотрю, что выбрал пользователь
                    if 'S' in possible_acts:  # Проверяю, можем ли мы сделать это действие
                        self.pl_x += 1  # Двигаю игрока
                        self.update_v()  # Обновляю карту
                        self.pretty_print_v()  # Вывожу изученную карту
                        return
                case 'W':  # Смотрю, что выбрал пользователь
                    if 'W' in possible_acts:  # Проверяем, можем ли мы сделать это действие
                        self.pl_y -= 1  # Двигаю игрока
                        self.update_v()  # Обновляю карту
                        self.pretty_print_v()  # Вывожу изученную карту
                        return
        match act:  # Смотрю действия, выбранные пользователем, если он никуда не подвинулся или не мог двигаться
            case 'I':  # Смотрю, что выбрал пользователь
                if 'I' in possible_acts:  # Проверяем, можем ли мы сделать это действие
                    print("")  # Стильная пустая строка
                    if len(player.get_inv().items) > 0:  # Если инвентарь не пустой - вывожу предметы
                        print('Ваш инвентарь: ' + ", ".join(player.get_inv().get_names()))
                    else:  # Если инвентарь пустой - сообщаю об этом
                        print('Ваш инвентарь пустой')
                    return
            case 'F':  # Смотрю, что выбрал пользователь
                if 'F' in possible_acts:  # Проверяем, можем ли мы сделать это действие
                    print("WiP")
                    self.fight()
            case 'GA':  # Смотрю, что выбрал пользователь
                if 'GA' in possible_acts:  # Проверяем, можем ли мы сделать это действие
                    if self.go_away_chance(stage) >= random():
                        randomized = choice(self.check_walls())
                        self.get_cell(self.pl_y, self.pl_x).set_is_dangerous(True)
                        self.force_move(randomized)
                        print('Вы случайно сбежали на ' + randomized)
                        return
                    else:
                        self.fight()
        self.update_v()  # Обновляю карту
        self.pretty_print_v()  # Вывожу изученную карту

    def force_move(self, side):
        match str(side):  # Смотрю действия, выбранные пользователем, если он может двигаться
            case 'N':  # Смотрю, что выбрал пользователь
                self.pl_x -= 1  # Двигаю игрока
                self.update_v()  # Обновляю карту
                self.pretty_print_v()  # Вывожу изученную карту
                return
            case 'E':  # Смотрю, что выбрал пользователь
                self.pl_y += 1  # Двигаю игрока
                self.update_v()  # Обновляю карту
                self.pretty_print_v()  # Вывожу изученную карту
                return
            case 'S':  # Смотрю, что выбрал пользователь
                self.pl_x += 1  # Двигаю игрока
                self.update_v()  # Обновляю карту
                self.pretty_print_v()  # Вывожу изученную карту
                return
            case 'W':  # Смотрю, что выбрал пользователь
                self.pl_y -= 1  # Двигаю игрока
                self.update_v()  # Обновляю карту
                self.pretty_print_v()  # Вывожу изученную карту
                return

    def check_walls(self):
        y, x = self.pl_y, self.pl_x
        no_walls = []
        if self.checker(y, x - 1):  # Проверяю, может ли игрок двигаться на север
            no_walls += 'N'
        if self.checker(y, x + 1):  # Проверяю, может ли игрок двигаться на юг
            no_walls += 'S'
        if self.checker(y - 1, x):  # Проверяю, может ли игрок двигаться на запад
            no_walls += 'W'
        if self.checker(y + 1, x):  # Проверяю, может ли игрок двигаться на восток
            no_walls += 'E'
        return no_walls

    def get_possible_actions(self):  # Функция, выдающая доступные действия
        possible_actions = []
        y, x = self.pl_y, self.pl_x  # Получаю координаты игрока
        attributes = self.get_cell(y, x).items.get_att()  # Получаю свойства предметов на клетке с игроком

        if "no_away" not in attributes:  # Проверяю если клетка с игроком (не не) позволяет ему двигаться
            if self.checker(y, x - 1):  # Проверяю, может ли игрок двигаться на север
                possible_actions += 'N'
            if self.checker(y, x + 1):  # Проверяю, может ли игрок двигаться на юг
                possible_actions += 'S'
            if self.checker(y - 1, x):  # Проверяю, может ли игрок двигаться на запад
                possible_actions += 'W'
            if self.checker(y + 1, x):  # Проверяю, может ли игрок двигаться на восток
                possible_actions += 'E'

        if self.get_cell(y, x).items.get_enemies():  # Проверяю, есть ли на клетке с игроком враг
            possible_actions.append('F')
            possible_actions.append('GA')
        possible_actions.append('I')
        return possible_actions

    def go_away_chance(self, stage: int):  # Функция, считающая шанс убежать от монстра(ов)
        return 0.7 ** ((len(self.get_cell(self.pl_y, self.pl_x).items.get_enemies()) *
                        self.get_cell(self.pl_y, self.pl_x).items.get_medium_damage() * stage) /
                       (self.player.damage * self.player.agility))

    def fight(self): # Сражение
        attack_queue = self.get_cell(self.pl_y, self.pl_x).items.get_enemies()  # Создание порядка атак
        # for i in range(len(attack_queue)):
        #     attack_queue[i].update(id=i)
        attack_queue.append(dict(name='Pl', attributes=['Player'], specs=
                            dict(damage=self.player.damage, agility=self.player.agility, health=self.player.health),
                                 id=-1))  # Добавляю в порядок атак игрока

        #Сортирую порядок атак по ловкости участников битвы
        attack_queue = sorted(attack_queue, key=lambda x: x['specs']['agility'], reverse=True)

        # print(attack_queue)

        # while True:
        #     for i in range(len(attack_queue) - 1):
        #         if attack_queue[i]['specs']['health'] <= 0 and attack_queue[i]['id'] != -1:
        #             self.get_cell(self.pl_y, self.pl_x).items.get_enemies().pop(attack_queue[i]['id'])
        #             attack_queue.pop(i)
        #             i -= 1
        #         elif attack_queue[i]['specs']['health'] <= 0 and attack_queue[i]['id'] == -1:
        #             exit(1)
        #     break

    def quitgame(self, code=0): # Функция для выхода из игры и вывода сообщения, и возможно ещё чего-то WiP
        match code:
            case 0:
                print('Вы закончили игру')
            case 1:
                print('Вы сдохли')
