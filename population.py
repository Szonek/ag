import specimen

class Population:
    def __init__(self, array_of_float):
        self.array_of_float = array_of_float
        self.chromosome = [specimen.Specimen(x=values) for values in self.array_of_float]
        self.size = len(self.array_of_float)
        self.child = None
        if self.size != 0:
            self.__check_sizes()
        pass

    def __check_sizes(self):
        min_size = min(sp.i for sp in self.chromosome)
        max_size = max(sp.i for sp in self.chromosome)
        if min_size != max_size:
            raise ValueError('Not every speciman has the same size in population.')

    def append(self, array_of_floats):
        self.array_of_float.extend(array_of_floats)
        for i in range(len(array_of_floats)):
            self.chromosome.append(specimen.Specimen(x=array_of_floats[i]))
        self.size = len(self.array_of_float)
        if self.size != 0:
            self.__check_sizes()
        pass

    def add_child(self, population):
        self.child = population
        pass

