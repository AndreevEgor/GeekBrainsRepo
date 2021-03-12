class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': salary, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return f'{sum(self._income.values())}'


developer = Position('Ivan', 'Ivanov', 'developer', 80000, 20000)
print(developer.get_full_name())
print(developer.get_total_income())



