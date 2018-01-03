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



num_of_start_population = 10
i = 3
minn = 0
maxx = 1
wspolrzedne = []
for j in range(num_of_start_population):
    rand_arr = [random.uniform(minn, maxx) for k in range(i)]
    wspolrzedne.append(rand_arr)
max_iter = 10
ff=0

ploter =Plot()
ploter.addKind("hartman_1")
while ff<max_iter :
    f_x = []
    print(wspolrzedne)
    for j in range(num_of_start_population):
        f_x.append(functions.Hartman_1(wspolrzedne[j]))
    print('prawdziwe',f_x)
    if(-3.86 in f_x):
        break
    max_popul = max(f_x)
    f_x_a = []
    for j in range(num_of_start_population):
        f_x_a.append(max_popul - f_x[j])
    print(f_x_a)
    print(max(f_x_a))
    if min(f_x) <= 50:
        ploter.addData("hartman_1",min(f_x))


    last_f_x = scaling.Scaling.gowno_sigma(f_x_a, 2)

    #test_population = selection.Selection.gproportional(wspolrzedne,last_f_x)
    test_population = wspolrzedne
    population_after_cross = []
    N= len(wspolrzedne)
    for j in range(int(0.8 * N)):
        rand_dad = random.randint(0, N - 1)
        rand_mom = random.randint(0, N - 1)
        kid_1,kid_2 = crossingovers.Crossingovers.aritmetic(test_population[rand_dad],test_population[rand_mom])
        population_after_cross.append(kid_1)
        population_after_cross.append(kid_2)
    test_population.extend(population_after_cross)
    new_f_x = []
    for j in range(len(test_population)):
        new_f_x.append(functions.Hartman_1(test_population[j]))

    zipped = zip(new_f_x, test_population)
    sor = sorted(zipped)

    new_f_x_sorted = [point[0] for point in sor]
    new_test_population_sorted = [point[1] for point in sor]

    final_popul = []
    for j in range(num_of_start_population):
        final_popul.append(new_test_population_sorted[j])

    wspolrzedne = final_popul[:]
    ff+=1

print("iter",ff)
ploter.showPlot()