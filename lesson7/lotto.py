import os
import random as rnd
from termcolor import colored
from lotto_card import LottoCard

clear = lambda: os.system('cls')


class Lotto:
    def __init__(self):
        self.bag = list(range(1, 101))
        self.card_player = LottoCard.generate('Карта игрока')
        self.card_computer = LottoCard.generate('Карта компьютера')
        self.game_over = False

    def start(self):
        while not self.game_over and (not self.card_player.is_complete() or not self.card_computer.is_complete()):
            print(self.card_computer)
            print(self.card_player)
            nmb = self.bag.pop(rnd.randint(0, len(self.bag) - 1))
            print(colored(f'Следующий бочонок {nmb}', 'green'))
            action = int(input('Зачеркнуть на карточке или продолжить? <1-зачеркнуть, 2-продолжить>\n'))
            if action == 1:
                if self.card_player.has_number(nmb):
                    self.card_player.check_number(nmb)
                else:
                    self.game_over = True
            else:
                if self.card_player.has_number(nmb):
                    self.game_over = True

            self.card_computer.check_number(nmb)

            if self.card_computer.is_complete() or self.game_over and not self.card_player.is_complete():
                print(colored('Компьютер победил', 'red'))
            elif self.card_player.is_complete():
                print(colored('Ты победил', 'green'))
