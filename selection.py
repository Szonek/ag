import random


class Selection:
    def __init__(self):
        pass



    @staticmethod
    def tournament(population):
        new_population = []
        f_x = []
        ind = []
        dict_ind_f = {'f_x':f_x,'index':ind}
        N = len(population.chromosome)
        while(N>0):
            r_inv = int(random.uniform(1, N))
            dict_ind_f['index'] = [int(random.uniform(0, len(population.chromosome) - 1)) for i in range(r_inv)]
            for j in range(r_inv):
                dict_ind_f['f_x'].append(population.chromosome[dict_ind_f['index'][j]].f_x)
            max_value = max(dict_ind_f['f_x'])
            index_of_max_value = dict_ind_f['index'][dict_ind_f['f_x'].index(max_value)]
            new_population.append(population.chromosome[index_of_max_value].x)
            dict_ind_f['index'] = []
            dict_ind_f['f_x'] = []
            N=N-1

        return new_population




    @staticmethod
    def proportional(population):
        print("To do")



