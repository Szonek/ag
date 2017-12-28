import specimen
import random


class Crossingovers:
    def __init__(self):
        pass

    @ staticmethod
    def aritmetic(vr, vs):
        a = random.uniform(0, 1)
        vr_prim = []
        vs_prim = []
        func = lambda x, y: a * x + (1 - a) * y
        for i in range(vr.i):
            vr_prim.append(func(vr.x[i], vs.x[i]))
            vs_prim.append(func(vs.x[i], vr.x[i]))

        return specimen.Specimen(x=vr_prim), specimen.Specimen(x=vs_prim)




    @ staticmethod
    def mixed(vr, vs):
        vr_prim = [vr.x[0]]
        vs_prim = [vs.x[0]]
        for i in range(1, vr.i):
            a = random.uniform(0, 1)
            func = lambda x, y: a * x + (1 - a) * y
            vr_prim.append(func(vr.x[i], vs.x[i]))
            vs_prim.append(func(vs.x[i], vr.x[i]))

        return specimen.Specimen(x=vr_prim), specimen.Specimen(x=vs_prim)