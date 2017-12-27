import event
import functions
import time
import specimen
import crossingovers

def example(print_full_table):
    s6 = specimen.Specimen(6, 0, 1)
    s6_2 = specimen.Specimen(6, 0, 1)
    s4 = specimen.Specimen(4, 0, 1)
    s2 = specimen.Specimen(2, 0, 1)



    #example of crossingover
    vr_prim, vs_prim = crossingovers.Crossingovers.aritmetic(s6, s6_2)
    print(vr_prim)
    print(vs_prim)

    #example of event profiling
    e1 = event.Event("Goldstein")
    e1.start()
    e1.add_result(functions.Goldstein_Price(s2.x))
    time.sleep(0.1) #zeby nie bylo end - start = 0
    e1.stop()

    e2 = event.Event("Hartman 1")
    e2.start()
    e2.add_result(functions.Hartman_1(s4.x))
    time.sleep(0.1) #zeby nie bylo end - start = 0
    e2.stop()

    e3 = event.Event("Hartman 2")
    e3.start()
    e3.add_result(functions.Hartman_2(s6.x))
    time.sleep(0.1) #zeby nie bylo end - start = 0
    e3.stop()

    e4 = event.Event("Shekel 1")
    e4.start()
    e4.add_result(functions.Shekel_1(s4.x))
    time.sleep(0.1) #zeby nie bylo end - start = 0
    e4.stop()

    e5 = event.Event("Shekel 2")
    e5.start()
    e5.add_result(functions.Shekel_1(s4.x))
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