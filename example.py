import event
import functions
import time
import stategies
import crossingovers
import mutation
import population
import random
import selection
import scaling
from Plot import Plot

#  example of Goldstain Price
def full_example():
    ploter =Plot()
    num_of_start_population = 10
    i = 2
    min = -2
    max = 2
    chance_for_crossingover = 0.5
    popul = population.Population([])
    #step 1 - random start population
    for j in range(num_of_start_population):
        rand_arr = [random.uniform(min, max) for k in range(i)]
        popul.append([rand_arr])

    #step 1b - calculate f_x
    '''
    for j in range(num_of_start_population):
        popul.chromosome[j].f_x = functions.Goldstein_Price(popul.chromosome[j].x)
        ploter.addData('przed', popul.chromosome[j].f_x)

    print(popul.get_max_f_x())

    #step 2 - make selection
    test_population = selection.Selection.proportional(popul)
    print(test_population)
    population_after_selection = population.Population(test_population)
    #step 3 - crossingover and mutation of best specimens in population
    #kryzwanie na wyseekcjonowanych rodziach
    #mutacje sie robi na potmokach(z krzyzywaonia) zeby je zmienic
    #ponizej testowo
    child_population = population.Population([])
    for j in range(int(0.5*chance_for_crossingover*num_of_start_population)):
        rand_dad = random.randint(0, num_of_start_population-1)
        rand_mom = random.randint(0, num_of_start_population-1)
        kid = crossingovers.Crossingovers.aritmetic(population_after_selection.chromosome[rand_dad], population_after_selection.chromosome[rand_mom])
        child_population.append(kid)
        child_population.append([population_after_selection.chromosome[rand_dad].x, population_after_selection.chromosome[rand_mom].x])
    if child_population.size != num_of_start_population:
        rand_dad = random.randint(0, num_of_start_population-1)
        rand_mom = random.randint(0, num_of_start_population-1)
        child_population.append([population_after_selection.chromosome[rand_dad].x, population_after_selection.chromosome[rand_mom].x])
    print(child_population)
    after_mutation = mutation.Mutation.reciprocal_exchange(0.5, child_population.array_of_float)
    child_population_after_mutation = population.Population(after_mutation)
    ploter.addKind('po')
    #step 3b - calculate f_x
    #for j in range(child_population_after_mutation.size):
    #    child_population_after_mutation.chromosome[j].f_x = functions.Goldstein_Price(child_population_after_mutation.chromosome[j].x)
    #    ploter.addData('po', child_population_after_mutation.chromosome[j].f_x)
    popul.add_child(child_population_after_mutation)

    #step 4 - stategis to choose new population from the old one
    popul = stategies.Strategies.full(popul)
    print(popul.chromosome[1].f_x)
    '''
    func = functions.Goldstein_Price
    func_mutation = mutation.Mutation.reciprocal_exchange
    func_crossingovers = crossingovers.Crossingovers.aritmetic
    func_selection = selection.Selection.tournament
    computing_loop(func,popul,10,ploter,'Randomowa',100,func_selection,0.8,func_crossingovers,func_mutation,0.8)
    ploter.showPlot()
    pass


def computing_loop(function ,popul, N, ploter, name_for_plot, number_of_iterations, selection_type,
                   probalility_of_crossingovers, crossingovers_type, mutation_type, probalility_of_mutation,
                   parameter_for_mutation=0, min_max_mutation=0, scale_c=2):
    ploter.addKind(name_for_plot)
    i = 0
    while i<number_of_iterations:
        for j in range(N):
            popul.chromosome[j].f_x = function(popul.chromosome[j].x)

        ploter.addData(name_for_plot, popul.get_max_f_x())
        print(popul.get_max_f_x())

        #make sigma-cutting scaling
        scaling.Scaling.sigma_cutting(popul, scale_c)

        #step 2 - make selection
        test_population = selection_type(popul)
        population_after_selection = population.Population(test_population)
        #step 3 - crossingover and mutation of best specimens in population
        #kryzwanie na wyseekcjonowanych rodziach
        #ponizej testowo
        child_population = population.Population([])
        for j in range(int(0.5*probalility_of_crossingovers*N)):
            rand_dad = random.randint(0, N-1)
            rand_mom = random.randint(0, N-1)
            kid = crossingovers_type(population_after_selection.chromosome[rand_dad], population_after_selection.chromosome[rand_mom])
            child_population.append(kid)
            child_population.append([population_after_selection.chromosome[rand_dad].x, population_after_selection.chromosome[rand_mom].x])
        if child_population.size != N:
            rand_dad = random.randint(0, N-1)
            rand_mom = random.randint(0, N-1)
            child_population.append([population_after_selection.chromosome[rand_dad].x, population_after_selection.chromosome[rand_mom].x])
        after_mutation = mutation_type(probalility_of_mutation, child_population.array_of_float)
        child_population_after_mutation = population.Population(after_mutation)
        #step 3b - calculate f_x
        #for j in range(child_population_after_mutation.size):
        #    child_population_after_mutation.chromosome[j].f_x = functions.Goldstein_Price(child_population_after_mutation.chromosome[j].x)
        #    ploter.addData('po', child_population_after_mutation.chromosome[j].f_x)
        popul.add_child(child_population_after_mutation)

        #step 4 - stategis to choose new population from the old one
        popul = stategies.Strategies.full(popul)
        i+=1


def main():
    print_full_table = True
    #TODO
    full_example()
    pass

if __name__ == "__main__":
    main()