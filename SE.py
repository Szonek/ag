import random
import math
import specimen

"""
-przetwarzany jes osobnik haploidalny z kodowaniem multialleicznym
-osobnik jest modyfikowany poprzez mutacje fenotypowa z rozkladem normalnym
"""
class SE_1_plus_1:
    def __init__(self, function, iterations=100, i=4, min=-100, max=100):
        self.function = function
        self.min = min
        self.max = max
        self.x = []  #pierwszy osobnik
        self.x_prim = []  #zmutowany osobnik
        self.s = 0  #liczba sukcesow
        self.num_mutations = 0  #ogolina liczba mutacji
        self.f_x = 0  #funkcja przystosowania
        self.f_x_prim = 0  #funkcja przystowania zmutowanego osobnika
        self.i = i  #dlugosc fenotypu
        self.max_iterations=iterations  #liczba iteracji
        self.iter = 0  #aktualian liczba iteracji
        self.epsilon = 0 #liczba losowa wg rozkladu normalnego
        self.r = 1  #zasieg mutacji
        pass


    def __step1(self):
        self.x = [random.uniform(self.min, self.max) for x in range(self.i)]
        pass

    def __step2(self):
        self.f_x = self.function(self.x)
        #self.f_x = functions.fun1(self.x)
        pass

    def __step3(self):
        self.iter += 1
        self.x_prim = []
        if self.iter == self.max_iterations:
            return True
        else:
            return False

    def __step4(self):
        self.num_mutations += 1
        self.epsilon = random.gauss(0, 1)
        for i in range(self.i):
            self.x_prim.append(self.x[i] + self.r*self.epsilon)
            if self.x_prim[-1] > self.max:
                self.x_prim[-1] = 100
            if self.x_prim[-1] < self.min:
                self.x_prim[-1] = -100
        pass

    def __step5(self):
        #self.f_x_prim = functions.fun1(self.x_prim)
        self.f_x_prim = self.function(self.x_prim)
        pass

    def __step6(self):
        if self.f_x_prim > self.f_x:
            self.x = self.x_prim
            self.f_x = self.f_x_prim
            self.s += 1
        pass

    def __step7(self):
        ratio = 1/5*self.num_mutations

        if self.s > ratio:
            self.r = (1/0.82)*self.epsilon
        elif self.s < ratio:
            self.r = 0.82*self.epsilon
        elif self.s == ratio:
            pass
        pass

    def run(self):
        self.__step1()
        self.__step2()
        finish = False
        while finish is False:
            finish = self.__step3()
            self.__step4()
            self.__step5()
            self.__step6()
            self.__step7()
        return self.f_x


class SE_u_plus_y:
    def __init__(self, function, mi, gamma, iterations=100, i=4, min=-100, max=100):
        self.function = function
        self.mi = mi
        self.gamma = gamma
        self.i = i
        self.max_iterations = iterations
        self.iter = 0
        self.min = min
        self.max = max
        self.species = []
        self.parents = []
    pass

    def __step1(self):
        self.species = [specimen.Diploidal_Specimen(self.i, self.min, self.max) for x in range(self.mi)]
        pass

    def __step2(self):
        for i in range(self.mi):
            self.species[i].f_x = self.function(self.species[i].v1)
        pass

    def __step3(self):
        self.iter += 1
        self.parents = []
        if self.iter == self.max_iterations:
            return True
        else:
            return False

    def __step4(self):
        for it in range(int(self.gamma)):
            rand_index = random.randint(0, self.mi-1)
            self.parents.append(self.species[rand_index])
        pass

    def run(self):
        self.__step1()
        self.__step2()
        finish = False
        while finish is False:
            finish = self.__step3()
            self.__step4()
        pass