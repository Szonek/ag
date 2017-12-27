import math


def fun1(x):
    result = 0
    for i in range(len(x)):
        result += math.pow(x[i], 2)
    return result


def Goldstein_Price(arr_val):
    def _job1(arr_val):
        return 1 + (arr_val[0] + arr_val[1] + 1) ** 2 * (
            19 - 14 * arr_val[0] + 3 * arr_val[0] ** 2 - 14 * arr_val[1] + 6 * arr_val[0] * arr_val[1] + 3 * arr_val[1] ** 2)


    def _job2(arr_val):
        return 30 + (2 * arr_val[0] - 3 * arr_val[1]) ** 2 * (
            18 - 32 * arr_val[0] + 12 * arr_val[0] ** 2 + 48 * arr_val[1] - 36 * arr_val[0] * arr_val[1] + 27 * arr_val[1] ** 2)

    return _job1(arr_val) * _job2(arr_val)



def Hartman_1(arr_val):
    factors_arr_val = [{'a1': 3, 'a2': 10, 'a3': 30, 'c': 1, 'p1': 0.3689, 'p2': 0.1170, 'p3': 0.2673},
                     {'a1': 0.1, 'a2': 10, 'a3': 35, 'c': 1.2, 'p1': 0.4699, 'p2': 0.4387, 'p3': 0.7470},
                     {'a1': 3, 'a2': 10, 'a3': 30, 'c': 3, 'p1': 0.1091, 'p2': 0.8732, 'p3': 0.5547},
                     {'a1': 0.1, 'a2': 10, 'a3': 35, 'c': 3.2, 'p1': 0.03815, 'p2': 0.5743, 'p3': 0.8828}]

    def _job1(arr_val,wfactor):
        temp_sum = 0
        temp_sum= temp_sum + factors_arr_val[wfactor]['a1'] * math.pow((arr_val[0] - factors_arr_val[wfactor]['p1']), 2)
        temp_sum = temp_sum + factors_arr_val[wfactor]['a2'] * math.pow((arr_val[1] - factors_arr_val[wfactor]['p2']), 2)
        temp_sum = temp_sum + factors_arr_val[wfactor]['a3'] * math.pow((arr_val[2] - factors_arr_val[wfactor]['p3']), 2)
        return math.exp(-temp_sum)


    sum_temp = 0
    for x in range(len(factors_arr_val)):
        sum_temp = sum_temp + factors_arr_val[x]['c'] * _job1(arr_val, x)
    return sum_temp * -1



def Hartman_2(arr_val):
    factors_arr_val = [{'a1': 10, 'a2': 3, 'a3': 17, 'a4': 3.5, 'a5': 1.7, 'a6': 8, 'c': 1, 'p1': 0.1313, 'p2': 0.1696,
                    'p3': 0.5569,'p4': 0.0124, 'p5': 0.8283, 'p6': 0.5886},
                     {'a1': 0.1, 'a2': 0.05, 'a3': 17, 'a4': 0.1, 'a5': 8, 'a6': 14, 'c': 1.2, 'p1': 0.2329,'p2': 0.4135,
                      'p3': 0.8307,'p4': 0.3736, 'p5': 0.1004, 'p6': 0.9991},
                     {'a1': 3, 'a2': 3.5, 'a3': 1.7, 'a4': 10, 'a5': 17, 'a6': 8, 'c': 3, 'p1': 0.2348, 'p2': 0.1415,
                      'p3': 0.3522,'p4': 0.2883, 'p5': 0.3047, 'p6': 0.6650},
                     {'a1': 17, 'a2': 8, 'a3': 0.05, 'a4': 10, 'a5': 0.1, 'a6': 14, 'c': 3.2, 'p1': 0.4047,'p2': 0.8828,
                      'p3': 0.8732,'p4': 0.5743, 'p5': 0.1091, 'p6': 0.0381}
                     ]

    def _job1(arr_val,wfactor):
        temp_sum = 0
        temp_sum= temp_sum + factors_arr_val[wfactor]['a1'] * math.pow(
            (arr_val[0] - factors_arr_val[wfactor]['p1']), 2)
        temp_sum = temp_sum + factors_arr_val[wfactor]['a2'] * math.pow(
            (arr_val[1] - factors_arr_val[wfactor]['p2']), 2)
        temp_sum = temp_sum + factors_arr_val[wfactor]['a3'] * math.pow(
            (arr_val[2] - factors_arr_val[wfactor]['p3']), 2)
        temp_sum = temp_sum + factors_arr_val[wfactor]['a4'] * math.pow(
            (arr_val[3] - factors_arr_val[wfactor]['p4']), 2)
        temp_sum = temp_sum + factors_arr_val[wfactor]['a5'] * math.pow(
            (arr_val[4] - factors_arr_val[wfactor]['p5']), 2)
        temp_sum = temp_sum + factors_arr_val[wfactor]['a6'] * math.pow(
            (arr_val[5] - factors_arr_val[wfactor]['p6']), 2)
        return math.exp(-temp_sum)
    sum_temp = 0
    for x in range(len(factors_arr_val)):
        sum_temp = sum_temp + factors_arr_val[x]['c'] * _job1(arr_val, x)
    return sum_temp * -1




def Shekel_1(arr_val):
    factors_arr_val = [{'a1': 4, 'a2': 4, 'a3': 4, 'a4': 4, 'c': 0.1},
                     {'a1': 1, 'a2': 1, 'a3': 1, 'a4': 1, 'c': 0.2},
                     {'a1': 8, 'a2': 8, 'a3': 8, 'a4': 8, 'c': 0.2},
                     {'a1': 6, 'a2': 6, 'a3': 6, 'a4': 6, 'c': 0.4},
                     {'a1': 3, 'a2': 7, 'a3': 3, 'a4': 7, 'c': 0.6}]

    sum_temp = 0
    for x in range(len(factors_arr_val)):
        sum_temp = sum_temp + _shekel_job1(arr_val, x,factors_arr_val)

    return sum_temp * -1



def Shekel_2(arr_val):
    factors_arr_val = [{'a1': 4, 'a2': 4, 'a3': 4, 'a4': 4, 'c': 0.1},
                     {'a1': 1, 'a2': 1, 'a3': 1, 'a4': 1, 'c': 0.2},
                     {'a1': 8, 'a2': 8, 'a3': 8, 'a4': 8, 'c': 0.2},
                     {'a1': 6, 'a2': 6, 'a3': 6, 'a4': 6, 'c': 0.4},
                     {'a1': 3, 'a2': 7, 'a3': 3, 'a4': 7, 'c': 0.6},
                     {'a1': 2, 'a2': 9, 'a3': 2, 'a4': 9, 'c': 0.6},
                     {'a1': 5, 'a2': 5, 'a3': 3, 'a4': 3, 'c': 0.3}]


    sum_temp = 0
    for x in range(len(factors_arr_val)):
        sum_temp = sum_temp + _shekel_job1(arr_val, x,factors_arr_val)

    return sum_temp * -1



def _shekel_job1(arr_val,wfactor,factors_arr_val):
    temp_sum = 0
    temp_sum= temp_sum + math.pow((arr_val[0] - factors_arr_val[wfactor]['a1']), 2)
    temp_sum= temp_sum + math.pow((arr_val[1] - factors_arr_val[wfactor]['a2']), 2)
    temp_sum= temp_sum + math.pow((arr_val[2] - factors_arr_val[wfactor]['a3']), 2)
    temp_sum= temp_sum + math.pow((arr_val[3] - factors_arr_val[wfactor]['a4']), 2) + factors_arr_val[wfactor]['c']
    return math.pow(temp_sum,-1)
