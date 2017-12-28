import random



class Specimen:
    def __init__(self, x=[]):
        self.i = len(x)
        self.x = x[:]
        self.v = self.x
        self.f_x = 0
        pass