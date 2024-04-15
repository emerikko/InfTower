import world as w
import Interface
from random import randint

# Задаю размер мира со стенками
y, x = 5, 10

# Генерирую мир
world = w.World(y, x)
# Сколько этажей пройдено
stage = 1

# Больше драконов богу драконов
for _ in range(15):
    world.get_cell(y=randint(1, world.height - 2), x=randint(1, world.width - 2)).items.append_item('Злой Дракон',
                                                                                                      ['fightable', 'no_away'],
                                                                                                      randint(1, 3) * stage)

# Добавляю в инвентарь бесполезные предметы для теста
world.player.add_item('SomeItem1', ['None'])
world.player.add_item('SomeItem2', ['None'])

# Вывожу весь мир, потому что могу
world.pretty_print()

# Стильная пустая строка
for i in range(100):  # Чтобы был эффект, что карта обновляется
    print("")

# Вывожу изученный мир
world.pretty_print_v()

# Игровой процесс
while True:
    Interface.write_available_actions(world, stage)  # Вызываю отрисовку интерфейса
    print("")  # Стильная пустая строка

    world.action(input('Выберите, что вы хотите сделать: '), stage)  # Выбор
    print("")  # Ещё одна стильная пустая строка
