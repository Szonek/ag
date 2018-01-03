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
i = 2
min = -2
maxx = 2
wspolrzedne = []
for j in range(num_of_start_population):
    rand_arr = [random.uniform(min, maxx) for k in range(i)]
    wspolrzedne.append(rand_arr)
max_iter =1000
ff=0

ploter =Plot()
ploter.addKind("dupa")
while ff<max_iter :
    f_x = []
    print(wspolrzedne)
    for j in range(num_of_start_population):
        f_x.append(functions.Goldstein_Price(wspolrzedne[j]))
    print('prawdziwe',f_x)
    if(3 in f_x):
        break
    max_popul = max(f_x)
    f_x_a = []
    for j in range(num_of_start_population):
        f_x_a.append(max_popul - f_x[j])
    print(f_x_a)
    print(max(f_x_a))
    ploter.addData("dupa",max(f_x_a))


    last_f_x = scaling.Scaling.gowno_sigma(f_x_a, 2)

    test_population = selection.Selection.gproportional(wspolrzedne,last_f_x)
    N= len(wspolrzedne)
    for j in range(int(0.8 * N)):
        rand_dad = random.randint(0, N - 1)
        rand_mom = random.randint(0, N - 1)
        test_population[rand_dad],test_population[rand_mom] = crossingovers.Crossingovers.aritmetic(test_population[rand_dad],test_population[rand_mom])

    wspolrzedne = test_population[:]
    ff+=1

print("iter",ff)
ploter.showPlot()