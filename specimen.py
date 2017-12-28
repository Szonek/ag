import random



class Specimen:
    def __init__(self, N, size_chromosome, min=-1, max=-1, x=[]):
        self.i = N
        self.g = size_chromosome
        self.x = x[:]
        if len(self.x) == 0:
            for j in range(self.i):
                self.x.append([random.uniform(min, max) for i in range(size_chromosome)])
        self.v = self.x
        self.f_x = 0