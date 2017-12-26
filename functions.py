import math


def fun1(x):
    result = 0
    for i in range(len(x)):
        result += math.pow(x[i], 2)
    return result


def Goldstein_Price(table):
    def _job1(table):
        return 1 + (table[0] + table[1] + 1) ** 2 * (
            19 - 14 * table[0] + 3 * table[0] ** 2 - 14 * table[1] + 6 * table[0] * table[1] + 3 * table[1] ** 2)


    def _job2(table):
        return 30 + (2 * table[0] - 3 * table[1]) ** 2 * (
            18 - 32 * table[0] + 12 * table[0] ** 2 + 48 * table[1] - 36 * table[0] * table[1] + 27 * table[1] ** 2)

    return _job1(table) * _job2(table)



def Hartman_1(table):
    factors_table = [{'a1': 3, 'a2': 10, 'a3': 30, 'c': 1, 'p1': 0.3689, 'p2': 0.1170, 'p3': 0.2673},
                     {'a1': 0.1, 'a2': 10, 'a3': 35, 'c': 1.2, 'p1': 0.4699, 'p2': 0.4387, 'p3': 0.7470},
                     {'a1': 3, 'a2': 10, 'a3': 30, 'c': 3, 'p1': 0.1091, 'p2': 0.8732, 'p3': 0.5547},
                     {'a1': 0.1, 'a2': 10, 'a3': 35, 'c': 3.2, 'p1': 0.03815, 'p2': 0.5743, 'p3': 0.8828}]

    def _job1(table,wfactor):
        temp_sum = 0
        temp_sum= temp_sum + factors_table[wfactor]['a1'] * math.pow((table[0] - factors_table[wfactor]['p1']), 2)
        temp_sum = temp_sum + factors_table[wfactor]['a2'] * math.pow((table[1] - factors_table[wfactor]['p2']), 2)
        temp_sum = temp_sum + factors_table[wfactor]['a3'] * math.pow((table[2] - factors_table[wfactor]['p3']), 2)
        return math.exp(-temp_sum)


    sum_temp = 0
    for x in range(len(factors_table)):
        sum_temp = sum_temp + factors_table[x]['c'] * _job1(table, x)
    return sum_temp * -1



def Hartman_2(table):
    factors_table = [{'a1': 10, 'a2': 3, 'a3': 17, 'a4': 3.5, 'a5': 1.7, 'a6': 8, 'c': 1, 'p1': 0.1313, 'p2': 0.1696,
                    'p3': 0.5569,'p4': 0.0124, 'p5': 0.8283, 'p6': 0.5886},
                     {'a1': 0.1, 'a2': 0.05, 'a3': 17, 'a4': 0.1, 'a5': 8, 'a6': 14, 'c': 1.2, 'p1': 0.2329,'p2': 0.4135,
                      'p3': 0.8307,'p4': 0.3736, 'p5': 0.1004, 'p6': 0.9991},
                     {'a1': 3, 'a2': 3.5, 'a3': 1.7, 'a4': 10, 'a5': 17, 'a6': 8, 'c': 3, 'p1': 0.2348, 'p2': 0.1415,
                      'p3': 0.3522,'p4': 0.2883, 'p5': 0.3047, 'p6': 0.6650},
                     {'a1': 17, 'a2': 8, 'a3': 0.05, 'a4': 10, 'a5': 0.1, 'a6': 14, 'c': 3.2, 'p1': 0.4047,'p2': 0.8828,
                      'p3': 0.8732,'p4': 0.5743, 'p5': 0.1091, 'p6': 0.0381}
                     ]

    def _job1(table,wfactor):
        temp_sum = 0
        temp_sum= temp_sum + factors_table[wfactor]['a1'] * math.pow(
            (table[0] - factors_table[wfactor]['p1']), 2)
        temp_sum = temp_sum + factors_table[wfactor]['a2'] * math.pow(
            (table[1] - factors_table[wfactor]['p2']), 2)
        temp_sum = temp_sum + factors_table[wfactor]['a3'] * math.pow(
            (table[2] - factors_table[wfactor]['p3']), 2)
        temp_sum = temp_sum + factors_table[wfactor]['a4'] * math.pow(
            (table[3] - factors_table[wfactor]['p4']), 2)
        temp_sum = temp_sum + factors_table[wfactor]['a5'] * math.pow(
            (table[4] - factors_table[wfactor]['p5']), 2)
        temp_sum = temp_sum + factors_table[wfactor]['a6'] * math.pow(
            (table[5] - factors_table[wfactor]['p6']), 2)
        return math.exp(-temp_sum)
    sum_temp = 0
    for x in range(len(factors_table)):
        sum_temp = sum_temp + factors_table[x]['c'] * _job1(table, x)
    return sum_temp * -1




def Shekel_1(table):
    factors_table = [{'a1': 4, 'a2': 4, 'a3': 4, 'a4': 4, 'c': 0.1},
                     {'a1': 1, 'a2': 1, 'a3': 1, 'a4': 1, 'c': 0.2},
                     {'a1': 8, 'a2': 8, 'a3': 8, 'a4': 8, 'c': 0.2},
                     {'a1': 6, 'a2': 6, 'a3': 6, 'a4': 6, 'c': 0.4},
                     {'a1': 3, 'a2': 7, 'a3': 3, 'a4': 7, 'c': 0.6}]

    sum_temp = 0
    for x in range(len(factors_table)):
        sum_temp = sum_temp + _shekel_job1(table, x,factors_table)

    return sum_temp * -1



def Shekel_2(table):
    factors_table = [{'a1': 4, 'a2': 4, 'a3': 4, 'a4': 4, 'c': 0.1},
                     {'a1': 1, 'a2': 1, 'a3': 1, 'a4': 1, 'c': 0.2},
                     {'a1': 8, 'a2': 8, 'a3': 8, 'a4': 8, 'c': 0.2},
                     {'a1': 6, 'a2': 6, 'a3': 6, 'a4': 6, 'c': 0.4},
                     {'a1': 3, 'a2': 7, 'a3': 3, 'a4': 7, 'c': 0.6},
                     {'a1': 2, 'a2': 9, 'a3': 2, 'a4': 9, 'c': 0.6},
                     {'a1': 5, 'a2': 5, 'a3': 3, 'a4': 3, 'c': 0.3}]


    sum_temp = 0
    for x in range(len(factors_table)):
        sum_temp = sum_temp + _shekel_job1(table, x,factors_table)

    return sum_temp * -1



def _shekel_job1(table,wfactor,factors_table):
    temp_sum = 0
    temp_sum= temp_sum + math.pow((table[0] - factors_table[wfactor]['a1']), 2)
    temp_sum= temp_sum + math.pow((table[1] - factors_table[wfactor]['a2']), 2)
    temp_sum= temp_sum + math.pow((table[2] - factors_table[wfactor]['a3']), 2)
    temp_sum= temp_sum + math.pow((table[3] - factors_table[wfactor]['a4']), 2) + factors_table[wfactor]['c']
    return math.pow(temp_sum,-1)
