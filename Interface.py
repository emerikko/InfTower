from Game.world import World

# Интерфейс

def write_available_actions(world: World, stage: int):
    possible_acts = world.get_possible_actions()  # Получаю действия, которые может сделать игрок

    # Вывожу действия, которые может сделать игрок
    if 'N' in possible_acts:
        print("[N] Вы можете пойти на север")
    if 'S' in possible_acts:
        print("[S] Вы можете пойти на юг")
    if 'E' in possible_acts:
        print("[E] Вы можете пойти на восток")
    if 'W' in possible_acts:
        print("[W] Вы можете пойти на запад")
    if 'I' in possible_acts:
        print("[I] Вы можете посмотреть инвентарь")
    if 'F' in possible_acts:
        print("[F] Вы можете сражаться с: " + ", ".join(world.get_cell(world.pl_y, world.pl_x).items.get_enemies_names()))
    if 'GA' in possible_acts:
        print("[GA] Вы можете попробовать убежать (" + str(round(world.go_away_chance(stage) * 100, 1)) + "%)")
    if 'GI' in possible_acts:
        print("[GI] Вы можете получить информацию о ваших характеристиках")
    #print("Ваше здоровье: " + str(world.get_player().get_health()))
    #print("Ваш урон: " + str(world.get_player().get_damage()))
    #print("Ваш уровень: " + str(world.get_player().get_lvl()))
