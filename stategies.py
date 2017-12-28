import population


class Strategies:
    def __init__(self):
        pass

    @staticmethod
    def full(popul):
        popul = popul.child
        return popul