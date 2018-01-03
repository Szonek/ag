import random
import math


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
    def gowno(popul,f_x):
        new_population = []
        temp = []
        N = len(popul)
        dict_ind_f = {'f_x': 0, 'index': 0}
        for j in range(N):
            dict_ind_f['f_x'] = f_x[j]
            dict_ind_f['index'] = j
            temp.append(dict_ind_f.copy())

        sorted_temp = sorted(temp, reverse=True, key=lambda tup: tup['f_x'])
        i = 0
        for j in range(N):
            if i==4:
                i =0
            new_population.append(popul[sorted_temp[i]['index']])
            i+=1
        return new_population



    @staticmethod
    def proportional(population):
        new_population = []
        N = len(population.chromosome)
        f_x = [population.chromosome[j].f_x for j in range(N)]
        min_value = min(f_x)
        population_sum = sum(f_x)
        func_probabilty = lambda x:x/population_sum
        p_s = [func_probabilty(f_x[j]) for j in range(N)]
        proportional_list = []
        proportional_dict = {'index':0, 'f_x':0, 'p_s':0}
        for i in range(N):
            proportional_dict['index'] = i
            proportional_dict['f_x'] = f_x[i]
            proportional_dict['p_s'] = p_s[i]
            proportional_list.append(proportional_dict.copy())
        new_proprtional_list = sorted(proportional_list, key=lambda proportional_list: proportional_list['p_s'])
        q_s = []
        for i in range(N):
            temp = new_proprtional_list[0]['p_s']
            for j in range(i):
                temp+=new_proprtional_list[j+1]['p_s']
            q_s.append(temp)
        for i in range(N):
            lucky_number = random.uniform(0,1)
            lucky_number_index = 0
            for j in range(N):
                if lucky_number <= q_s[j]:
                    lucky_number_index = j
                    break
            new_population.append(population.chromosome[lucky_number_index].x)
        return new_population







