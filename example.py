import event
import functions
import time
import specimen
import crossingovers
import mutation

def example(print_full_table):
    s2 = specimen.Specimen(6, 2, -2, 2)
    s4 = specimen.Specimen(6, 3, 0, 1)
    s6 = specimen.Specimen(6, 6, 0, 1)
    s61 = specimen.Specimen(6, 6, 0, 1)
    s6_2 = specimen.Specimen(6, 4, 0, 10)
    s6_21 = specimen.Specimen(6, 4, 0, 10)


    #example of mutation
    population = mutation.Mutation.value_uniform(0.5,-2,2,s2.x,1)
    #prawdopodobienstwo,min,max,populacja,ktory gen podmieniamy
    print(population)
    population = mutation.Mutation.reciprocal_exchange(0.5,s2.x)
    #prawdopodoienstwo,populacja
    print(population)

    #example of crossingover
    vr_prim, vs_prim = crossingovers.Crossingovers.aritmetic(s6_2, s6_21)
    print(vr_prim)
    print(vs_prim)

    vr_prim, vs_prim = crossingovers.Crossingovers.mixed(s6, s61)
    print(vr_prim)
    print(vs_prim)

    #example of event profiling
    e1 = event.Event("Goldstein")
    e1.start()
    for i in range(s2.i):
        e1.add_result(functions.Goldstein_Price(s2.x[i]))
    time.sleep(0.1) #zeby nie bylo end - start = 0
    e1.stop()

    e2 = event.Event("Hartman 1")
    e2.start()
    for i in range(s4.i):
        e2.add_result(functions.Hartman_1(s4.x[i]))
    time.sleep(0.1) #zeby nie bylo end - start = 0
    e2.stop()

    e3 = event.Event("Hartman 2")
    e3.start()
    for i in range(s6.i):
        e3.add_result(functions.Hartman_2(s6.x[i]))
    time.sleep(0.1) #zeby nie bylo end - start = 0
    e3.stop()

    e4 = event.Event("Shekel 1")
    e4.start()
    for i in range(s6_2.i):
        e4.add_result(functions.Shekel_1(s6_2.x[i]))
    time.sleep(0.1) #zeby nie bylo end - start = 0
    e4.stop()

    e5 = event.Event("Shekel 2")
    e5.start()
    for i in range(s6_2.i):
        e5.add_result(functions.Shekel_1(s6_2.x[i]))
    time.sleep(0.1) #zeby nie bylo end - start = 0
    e5.stop()

    p = event.Profiling("test", [e1, e2, e3, e4, e5])

    if(print_full_table):
        p.print_total_table()
    pass


def main():
    print_full_table = True
    #TODO
    example(print_full_table)
    pass

if __name__ == "__main__":
    main()