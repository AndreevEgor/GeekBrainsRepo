from abc import abstractmethod


class Clothes:
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expenditure(self):
        pass

    def __add__(self, other):
        return self.expenditure + other.expenditure


class Coat(Clothes):
    @property
    def expenditure(self):
        return round((self.param / 6.5 + 0.5), 2)


class Suit(Clothes):
    @property
    def expenditure(self):
        return round(((2 * self.param + 0.3) / 100), 2)


coat = Coat(50)
print(coat.expenditure)
suit = Suit(185)
print(suit.expenditure)
print(coat + suit)
