import items as it

# Клетка башни

class Cell:
    _blocked = False  # По умолчанию клетка не заблокирована
    _visited = False  # По умолчанию клетка не замечена
    _dangerous = False # По умолчанию безопасна

    def __init__(self):
        self._items = it.Items()  # Добавляю пустые предметы в клетку
        # for i in range(len(self._items)):
        #     self._items[i].update(id=i)
        pass

    def is_blocked(self):  # Возвращаю состояние клетки (заблокировано или нет)
        return self._blocked

    def set_is_blocked(self, _is_blocked: bool):  # Меняю состояние клетки на указанное (заблокировано или нет)
        self._blocked = _is_blocked

    def is_visited(self):  # Возвращаю состояние клетки (увидено или нет)
        return self._visited

    def set_is_visited(self, _is_visited: bool):  # Меняю состояние клетки на указанное (увидено или нет)
        self._visited = _is_visited

    def is_dangerous(self):  # Возвращаю состояние клетки (опасно или нет)
        return self._dangerous

    def set_is_dangerous(self, _is_dangerous: bool):  # Меняю состояние клетки на указанное (заблокировано или нет)
        self._dangerous = _is_dangerous

    @property
    def items(self):  # Получаю предметы внутри клетки
        return self._items
