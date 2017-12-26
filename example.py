import event
import SE
import functions

functions_map = {
        "fun1": functions.fun1
    }


def SE_1_plus_1(print_full_table=False):
    events = []
    iterations = [5, 10, 20, 50, 100, 1000, 10000]
    names = []
    for func_name, func in functions_map.items():
        names.append(func_name)
        for j in iterations:
            e = event.Event(func_name, j)
            s11 = SE.SE_1_plus_1(func, j)
            e.start()
            result = s11.run()
            e.add_result(result)
            e.stop()
            events.append(e)
    p = event.Profiling("SE_1_plus_1", events)
    if print_full_table:
        p.print_total_table()

def SE_u_plus_y(print_full_table=False):
    events = []
    iterations = [5, 10, 20, 50, 100, 1000, 10000]
    mi = [5, 10, 20, 50, 100, 1000, 10000]
    gamma = lambda g : [g/g, g/10, g/9, g/8, g/7, g/6, g/5, g/4, g/3, g/2]
    names = []
    se = SE.SE_u_plus_y(functions_map['fun1'], mi[3], gamma(mi[1])[6])
    se.run()
    # for func_name, func in functions_map.items():
    #     names.append(func_name)
    #     for j in iterations:
    #         e = event.Event(func_name, j)
    #         s11 = SE.SE_1_plus_1(func, j)
    #         e.start()
    #         result = s11.run()
    #         e.add_result(result)
    #         e.stop()
    #         events.append(e)
    # p = event.Profiling("SE_1_plus_1", events)
    # if print_full_table:
    #     p.print_total_table()


def main():
    print_full_table = True
    #TODO
    # - print optimal arguments
    # - finish se_u_plus_y
    SE_1_plus_1(print_full_table)
    SE_u_plus_y(print_full_table)
    pass

if __name__ == "__main__":
    main()