import event
import functions
import time
import specimen
import crossingovers
import mutation
import population

def example(print_full_table):
    s2 = specimen.Specimen(2, -2, 2)
    s4 = specimen.Specimen(3, 0, 1)
    s6 = specimen.Specimen(6, 0, 1)
    s61 = specimen.Specimen(6, 0, 1)
    s6_2 = specimen.Specimen(6, 0, 10)
    s6_21 = specimen.Specimen(6, 0, 10)

    #example of creating population
    start_population = population.Population([s6.x, s61.x, s6_2.x, s6_21.x])

    #example of mutation
    new_specimans = mutation.Mutation.value_uniform(0.5,-2,2,start_population.array_of_float,1)
    start_population.append(new_specimans)
    #prawdopodobienstwo,min,max,populacja,ktory gen podmieniamy

    new_specmans_2 = mutation.Mutation.reciprocal_exchange(0.5,start_population.array_of_float)
    #prawdopodoienstwo,populacja

    start_population.append(new_specmans_2)

    #example of crossingover
    vr_prim, vs_prim = crossingovers.Crossingovers.aritmetic(s6_2, s6_21)
    print(vr_prim.x)
    print(vs_prim.x)

    print(s6_21.x)
    vr_prim, vs_prim = crossingovers.Crossingovers.mixed(vr_prim, vs_prim)
    print(vr_prim.x)
    print(vs_prim.x)



    #example of event profiling
    p1 = event.Profiling("Goldstein")

    for i in range(start_population.size):
        e1 = event.Event5("Goldstein_" + str(i))
        e1.start()
        e1.add_result(functions.Goldstein_Price(start_population.array_of_float[i]))
        time.sleep(0.01) #zeby nie bylo end - start = 0
        e1.stop()
        p1.add_event(e1)


    p2 = event.Profiling("Hartman 1")

    for i in range(start_population.size):
        e2 = event.Event("Hartman_" + str(i))
        e2.start()
        e2.add_result(functions.Hartman_1(start_population.array_of_float[i]))
        time.sleep(0.01) #zeby nie bylo end - start = 0
        e2.stop()
        p2.add_event(e2)


    p3 = event.Profiling("Hartman 2")

    for i in range(start_population.size):
        e3 = event.Event("Hartman2_" + str(i))
        e3.start()
        e3.add_result(functions.Hartman_2(start_population.array_of_float[i]))
        time.sleep(0.01) #zeby nie bylo end - start = 0
        e3.stop()
        p3.add_event(e3)


    p4 = event.Profiling("Shekel_1")

    for i in range(start_population.size):
        e4 = event.Event("Shekel1_" + str(i))
        e4.start()
        e4.add_result(functions.Shekel_1(start_population.array_of_float[i]))
        time.sleep(0.01) #zeby nie bylo end - start = 0
        e4.stop()
        p4.add_event(e4)

    p5 = event.Profiling("Shekel_2")

    for i in range(start_population.size):
        e5 = event.Event("Shekel2_" + str(i))
        e5.start()
        e1.add_result(functions.Shekel_2(start_population.array_of_float[i]))
        time.sleep(0.01) #zeby nie bylo end - start = 0
        e5.stop()
        p5.add_event(e5)

    if(print_full_table):
        p1.print_total_table()
        p2.print_total_table()
        p3.print_total_table()
        p4.print_total_table()
        p5.print_total_table()
    pass


def main():
    print_full_table = True
    #TODO
    example(print_full_table)
    pass

if __name__ == "__main__":
    main()