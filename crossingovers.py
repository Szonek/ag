import specimen
import random


class Crossingovers:
    def __init__(self):
        pass

    @ staticmethod
    def aritmetic(vr, vs):
        a = 2
        vr_prim = []
        vs_prim = []
        func = lambda x, y: a * x + (1 - a) * y
        for i in range(len(vr)):
            vr_prim.append(func(vr[i], vs[i]))
            vs_prim.append(func(vs[i], vr[i]))

        if  vr_prim[0] in range(-2,2) and vr_prim[1] in range(-2,2) and vs_prim[0] in range(-2,2) and vs_prim[1] in range(-2,2):
            return vr_prim, vs_prim
        elif vr_prim[0] in range(-2,2) and vr_prim[1] in range(-2,2):
            return vr_prim,vs
        elif vs_prim[0] in range(-2,2) and vs_prim[1] in range(-2,2):
            return vr,vs_prim
        else:
            return vs,vr




    @ staticmethod
    def mixed(vr, vs):
        vr_prim = [vr.x[0]]
        vs_prim = [vs.x[0]]
        for i in range(1, vr.i):
            a = random.uniform(0, 1)
            func = lambda x, y: a * x + (1 - a) * y
            vr_prim.append(func(vr.x[i], vs.x[i]))
            vs_prim.append(func(vs.x[i], vr.x[i]))

        return vr_prim, vs_prim