# Предметы (Монстры, сокровища, что угодно)

class Items:
    items: list[dict]

    def __init__(self, items=None, specs=None):
        if items is None:
            items = []
        if specs is None:
            specs = dict(damage=0, agility=0, health=0, target=None)
        self.items = [dict(name='air', attributes=[], specs=specs)]
        self.items += items

# Создаю и добавляю предмет со свойствами
    def append_item(self, name: str, attributes: list, damage=0, agility=0, health=0, target=0):
        self.items.append(dict(name=name, attributes=attributes, specs=dict(damage=damage, agility=agility,
                                                                            health=health, target=target)))

    def append_items(self, items: list):  # Добавляю какие-то предметы
        self.items += items

    def get_att(self):  # Получаю свойства всех предметов
        atts = []
        for i in range(len(self.items)):
            atts += self.items[i]['attributes']
        return atts

    def get_enemies_names(self):  # Получаю врагов на клетке (со свойством 'fightable')
        enemies = []
        for i in range(len(self.items)):
            if 'fightable' in self.items[i]['attributes']:
                enemies.append(self.items[i]['name'])
        return enemies

    def get_enemies(self) -> list:  # Получаю врагов на клетке (со свойством 'fightable')
        enemies = list()
        for i in range(len(self.items)):
            if 'fightable' in self.items[i]['attributes']:
                enemies.append(self.items[i])
        return enemies

    def damage(self, enemy_num: int) -> int:
        return self.items[enemy_num]['specs']['damage']

    def agility(self, enemy_num: int) -> int:
        return self.items[enemy_num]['specs']['agility']

    def health(self, enemy_num: int) -> int:
        return self.items[enemy_num]['specs']['health']

    def target(self, enemy_num: int) -> int:
        return self.items[enemy_num]['specs']['target']

    def get_medium_damage(self):
        summary = 0
        count = 0
        for i in range(len(self.items)):
            summary += self.items[i]['specs']['damage']
            if self.items[i]['specs']['damage'] > 0:
                count += 1
        if count == 0:
            return 0
        return summary / count

    def get_names(self):  # Получаю имена всех предметов:
        names = []
        for i in range(len(self.items)):
            names.append(self.items[i]['name'])
        return names
