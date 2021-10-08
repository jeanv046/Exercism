from itertools import product
from random import choice
from string import ascii_uppercase as LETTERS
class Robot:
    name_pool = list(product(
        product(LETTERS, LETTERS),
        range(0, 1000)
    ))
    def __init__(self):
        self.reset()
    def reset(self):
        if not self.name_pool:
            raise RuntimeError("Out of names")
        alpha, numeric = choice(self.name_pool)
        self.name = ''.join(alpha) + "%03d" % numeric
        self.name_pool.remove((alpha, numeric))