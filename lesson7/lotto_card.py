import random as rnd
from termcolor import colored


class LottoCard:
    def __init__(self, title: str = 'Lotto Card', numbers: list = []):
        self.title = title
        self._numbers = numbers
        self.numbers_checked = []
        self._set_rows()
        pass

    @property
    def numbers(self) -> list:
        return self._numbers

    @numbers.setter
    def numbers(self, ls: list):
        self._numbers = ls
        self._set_rows()

    @staticmethod
    def generate(title: str):
        numbers = set()
        while len(numbers) < 15:
            numbers.add(rnd.randint(1, 100))
        ls = list(numbers)
        ls.sort()
        return LottoCard(title, ls)

    def check_number(self, nmb):
        if nmb in self.numbers and nmb not in self.numbers_checked:
            self.numbers_checked.append(nmb)

    def has_number(self, nmb):
        return nmb in self.numbers

    def _set_rows(self):
        self.__rows = [['' for y in list(range(10))] for x in range(3)]

        nmbs = [n // 10 for n in self.numbers]

        for i, nmb in enumerate(self.numbers):
            ls = self.__rows[i % 3][nmb // 10:]
            if '' in ls:
                index = ls.index('') + nmb // 10 if len(ls) > 0 else -1
                if self.__rows[i % 3][index] == '':
                    self.__rows[i % 3][index] = nmb
            else:
                index = 10 - list(reversed(self.__rows[i % 3])).index('')
                sub_list = self.__rows[i % 3][index:10]
                self.__rows[i % 3] = self.__rows[i % 3][:index - 1]
                self.__rows[i % 3] = self.__rows[i % 3] + sub_list
                self.__rows[i % 3].append(nmb)

    def _checked(self, nmb):
        _str = str(nmb).ljust(3)
        if nmb in self.numbers_checked:
            return colored(_str, 'green')
        else:
            return colored(_str, 'magenta')

    def is_complete(self):
        return len(self.numbers) == len(self.numbers_checked)

    def __str__(self):
        title = colored((self.title + ' ').ljust(29, '*'), 'magenta')
        s = [' '.join(map(lambda n: self._checked(n) if n != '' else ' ' + str(n), x)) for x in self.__rows]
        end = colored(''.ljust(29, '*'), 'magenta')
        return title + '\n' + '\n'.join(s) + '\n' + end
