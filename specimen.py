import random


class Diploidal_Specimen:
    def __init__(self, i, min, max):
        self.i = i
        self.v1 = []
        self.v2 = []
        for j in range(self.i):
            self.v1.append(random.uniform(min, max))
        self.f_x = 0
        pass