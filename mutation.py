import random
import copy

class Mutation:
    def __init__(self):
        pass

    @staticmethod
    def value_uniform(probalility, min, max, population, which_parameter):
        new_population = copy.deepcopy(population)
        count_to_mutation = int(len(new_population)*probalility)

        random_values = [random.uniform(min, max) for i in range(count_to_mutation)]
        random_inv = [int(random.uniform(0,len(new_population)-1)) for i in range(count_to_mutation)]

        for x in range(len(random_inv)):
            new_population[random_inv[x]][which_parameter] = random_values[x]

        return new_population

    @staticmethod
    def reciprocal_exchange(probalility, population):
        new_population = copy.deepcopy(population)
        count_to_mutation = int(len(new_population) * probalility)
        random_inv = [int(random.uniform(0, len(new_population))) for i in range(count_to_mutation)]
        random_first_position = [int(random.uniform(0,len(new_population[0]))) for i in range(count_to_mutation)]
        random_second_position = [int(random.uniform(0,len(new_population[0]))) for i in range(count_to_mutation)]

        for x in range(len(random_inv)):
            temp = new_population[random_inv[x]][random_first_position[x]]
            new_population[random_inv[x]][random_first_position[x]] = new_population[random_inv[x]][random_second_position[x]]
            new_population[random_inv[x]][random_second_position[x]] = temp

        return new_population

