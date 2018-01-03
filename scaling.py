import numpy as np




class Scaling:
    def __init__(self):
        pass

    @staticmethod
    def sigma_cutting(population, c):

        f_avg = sum(s.f_x for s in population.chromosome) / population.size

        temp = sum(np.power(s.f_x - f_avg, 2) for s in population.chromosome) / population.size
        sigma = np.sqrt(temp)

        for speci in population.chromosome:
            speci.f_x = speci.f_x + (f_avg - c*sigma)
        pass


    @staticmethod
    def gowno_sigma(f_x,c):
        f_avg = sum(f_x) / len(f_x)

        temp = sum(np.power(f_x[x] - f_avg, 2) for x in range(len(f_x))) / len(f_x)
        sigma =np.sqrt(temp)
        new_f_x = []
        for x in range(len(f_x)):
            new_f_x.append(f_x[x]+(f_avg-c*sigma))
        return new_f_x