import specimen
import random


class Crossingovers:
    def __init__(self):
        pass

    @ staticmethod
    def aritmetic(vr, vs):
        a = random.uniform(0, 1)

        func = lambda x, y : a*x + (1-a)*y

        vr_prim = [func(vr.x[i], vs.x[i]) for i in range(vr.i)]
        vs_prim = [func(vs.x[i], vr.x[i]) for i in range(vr.i)]

        return vr_prim, vs_prim