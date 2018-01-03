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