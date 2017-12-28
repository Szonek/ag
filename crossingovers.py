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
        for j in range(len(vr.x)):
            vr_prim.append([func(vr.x[j][i], vs.x[j][i]) for i in range(vr.g)])
            vs_prim.append([func(vs.x[j][i], vr.x[j][i]) for i in range(vr.g)])

        speci_vr_prim = specimen.Specimen(N=vr.i, size_chromosome=vr.g, x=vr_prim)
        speci_vs_prim = specimen.Specimen(N=vs.i, size_chromosome=vs.g, x=vs_prim)
        return speci_vr_prim, speci_vs_prim




    @ staticmethod
    def mixed(vr, vs):
        vr_prim = []
        vs_prim = []

        for j in range(vr.i):
            temp_vr_prim = [vr.x[j][0]]
            temp_vs_prim = [vs.x[j][0]]
            for i in range(1, vr.g):
                a = random.uniform(0, 1)
                func = lambda x, y: a * x + (1 - a) * y
                temp_vr_prim.append(func(vr.x[j][i], vs.x[j][i]))
                temp_vs_prim.append(func(vs.x[j][i], vr.x[j][i]))
            vr_prim.append(temp_vr_prim)
            vs_prim.append(temp_vs_prim)

        speci_vr_prim = specimen.Specimen(N=vr.i, size_chromosome=vr.g, x=vr_prim)
        speci_vs_prim = specimen.Specimen(N=vs.i, size_chromosome=vs.g, x=vs_prim)

        return speci_vr_prim, speci_vs_prim