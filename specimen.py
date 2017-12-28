import random



class Specimen:
    def __init__(self, N,size_chromosome, min, max):
        self.i = N
        self.g = size_chromosome
        self.x = []
        for j in range(self.i):
            self.x.append([random.uniform(min, max) for i in range(size_chromosome)])
        self.v = self.x
        self.f_x = 0

class Diploidal_Specimen:
    def __init__(self, i, min, max):
        self.i = i
        self.v1 = []
        self.v2 = []
        for j in range(self.i):
            self.v1.append(random.uniform(min, max))
        self.f_x = 0
        pass