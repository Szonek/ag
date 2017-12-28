import random



class Specimen:
    def __init__(self, N=-1, min=-1, max=-1, x=[]):
        if len(x) == 0:
            self.i = N
            self.x = [random.uniform(min, max) for i in range(self.i)]
            self.v = self.x
        else:
            self.i = len(x)
            self.x = x[:]
            self.v = self.x
        self.f_x = 0
        pass