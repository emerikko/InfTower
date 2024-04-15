import items as it

# Игрок

class Player:  # WiP
    # inv = it.Items()
    # health = 100
    # maxHealth = 100
    # damage = 1
    # agility = 1
    # lvl = 1

    def __init__(self, _inv=it.Items(), _health=100, _max_health=100, _damage=1, _agility=2, _lvl=1):
        self._inv = _inv
        self._health = _health
        self._max_health = _max_health
        self._damage = _damage
        self._agility = _agility
        self._lvl = _lvl
        pass

    def get_inv(self):
        return self._inv

    def add_item(self, name: str, attributes: list):
        self._inv.append_item(name, attributes)

    def add_items(self, items: list[dict]):
        self._inv.append_items(items)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health: int):
        self._health = new_health

    @property
    def max_health(self):
        return self._max_health

    @max_health.setter
    def max_health(self, new_max_health: int):
        self._max_health = new_max_health

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, new_damage: int):
        self._damage = new_damage

    @property
    def agility(self):
        return self._agility

    @agility.setter
    def agility(self, new_agility: int):
        self._agility = new_agility

    @property
    def lvl(self):
        return self._lvl

    @lvl.setter
    def lvl(self, new_lvl: int):
        self._lvl = new_lvl

    def update_health(self):
        if self._health > self._max_health:
            self._health = self._max_health
