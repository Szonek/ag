import event
import functions
import time
import stategies
import crossingovers
import mutation
import population
import random
import selection
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
                   parameter_for_mutation=0, min_max_mutation=0):
    ploter.addKind(name_for_plot)
    i = 0
    while i<number_of_iterations:
        for j in range(N):
            popul.chromosome[j].f_x = function(popul.chromosome[j].x)

        ploter.addData(name_for_plot, popul.get_max_f_x())
        print(popul.get_max_f_x())


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


def example(print_full_table):
    # s2 = specimen.Specimen(2, -2, 2)
    # s4 = specimen.Specimen(3, 0, 1)
    # s6 = specimen.Specimen(6, 0, 1)
    # s61 = specimen.Specimen(6, 0, 1)
    # s6_2 = specimen.Specimen(6, 0, 10)
    # s6_21 = specimen.Specimen(6, 0, 10)
    #
    # #example of creating population
    # start_population = population.Population([s6.x, s61.x, s6_2.x, s6_21.x])
    #
    # #example of mutation
    # child_population = population.Population([])
    # child_1 = mutation.Mutation.value_uniform(0.5,-2,2,start_population.array_of_float,1)
    # #prawdopodobienstwo,min,max,populacja,ktory gen podmieniamy
    #
    # child_2 = mutation.Mutation.reciprocal_exchange(0.5,start_population.array_of_float)
    # #prawdopodoienstwo,populacja
    #
    # child_population.append(child_1)
    # child_population.append(child_2)
    # start_population.add_child(child_population)
    #
    #
    # #example of crossingover
    # vr_prim, vs_prim = crossingovers.Crossingovers.aritmetic(s6_2, s6_21)
    # print(vr_prim.x)
    # print(vs_prim.x)
    #
    # print(s6_21.x)
    # vr_prim, vs_prim = crossingovers.Crossingovers.mixed(vr_prim, vs_prim)
    # print(vr_prim.x)
    # print(vs_prim.x)
    #
    #
    #
    # #example of event profiling
    # p1 = event.Profiling("Goldstein")
    #
    # for i in range(start_population.size):
    #     e1 = event.Event("Goldstein_" + str(i))
    #     e1.start()
    #     e1.add_result(functions.Goldstein_Price(start_population.array_of_float[i]))
    #     time.sleep(0.01) #zeby nie bylo end - start = 0
    #     e1.stop()
    #     p1.add_event(e1)
    #
    #
    # p2 = event.Profiling("Hartman 1")
    #
    # for i in range(start_population.size):
    #     e2 = event.Event("Hartman_" + str(i))
    #     e2.start()
    #     e2.add_result(functions.Hartman_1(start_population.array_of_float[i]))
    #     time.sleep(0.01) #zeby nie bylo end - start = 0
    #     e2.stop()
    #     p2.add_event(e2)
    #
    #
    # p3 = event.Profiling("Hartman 2")
    #
    # for i in range(start_population.size):
    #     e3 = event.Event("Hartman2_" + str(i))
    #     e3.start()
    #     e3.add_result(functions.Hartman_2(start_population.array_of_float[i]))
    #     time.sleep(0.01) #zeby nie bylo end - start = 0
    #     e3.stop()
    #     p3.add_event(e3)
    #
    #
    # p4 = event.Profiling("Shekel_1")
    #
    # for i in range(start_population.size):
    #     e4 = event.Event("Shekel1_" + str(i))
    #     e4.start()
    #     e4.add_result(functions.Shekel_1(start_population.array_of_float[i]))
    #     time.sleep(0.01) #zeby nie bylo end - start = 0
    #     e4.stop()
    #     p4.add_event(e4)
    #
    # p5 = event.Profiling("Shekel_2")
    #
    # for i in range(start_population.size):
    #     e5 = event.Event("Shekel2_" + str(i))
    #     e5.start()
    #     e1.add_result(functions.Shekel_2(start_population.array_of_float[i]))
    #     time.sleep(0.01) #zeby nie bylo end - start = 0
    #     e5.stop()
    #     p5.add_event(e5)
    #
    # if(print_full_table):
    #     p1.print_total_table()
    #     p2.print_total_table()
    #     p3.print_total_table()
    #     p4.print_total_table()
    #     p5.print_total_table()
    pass


def main():
    print_full_table = True
    #TODO
    example(print_full_table)
    full_example()
    pass

if __name__ == "__main__":
    main()