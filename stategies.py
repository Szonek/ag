import population
import copy


class Strategies:
    def __init__(self):
        pass

    @staticmethod
    def full(popul):
        popul = copy.deepcopy(popul.child)
        return popul