class Tomato:
    states = {0: 'nothing', 1: 'flower', 2: 'green', 3: 'red'}  #2.все стадии созревания

    def __init__(self, index):  #3.
        self._index = index
        self._state = 0

    def grow(self):   #4.следующая стадия созревания
        self._next_state_()

    def is_ripe(self):  #4.проверка созревания с защитой
        if self._state == 4:
            return True
        return False

    def _next_state_(self):
        if self._state < 3:
            self._state += 1
        self._print_state_()

    def _print_state_(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:


    def __init__(self, num):  #2
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):  #3
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):  #4
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):  #5
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):  #2
        self.name = name
        self._plant = plant

    def work(self):  #3
        print('Cадовник должен еще поработать')
        self._plant.grow_all()
        print('Томаты созрели')

    def harvest(self):  #4
        print('Можно собирать')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран')
        else:
            print('Предупреждение!!!еще зеленые')




    def knowledge_base():   #5
        print('Спаравка по садоводству')


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(3)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()