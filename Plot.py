import matplotlib.pyplot as plt


class Plot():

    KINDS = ['ro', 'go', 'bo', 'co', 'mo', 'yo', 'ko',
             'rx', 'gx', 'bx', 'cx', 'mx', 'yx', 'kx',
             'rs', 'gs', 'bs', 'cs', 'ms', 'ys', 'ks']


    def __init__(self):
        self.list_of_kinds = []
        self.Dict_for_data = {}
        self.max_kinds = len(self.KINDS)
        self.borders_for_plot = [1,0,0,0] #min and max in X-axis,min and max in Y-axis


    def addKind(self, name):

        if len(self.list_of_kinds) > self.max_kinds:
            print("To much kinds to display")
            return

        if name in self.list_of_kinds:
            print("Already have that kind")
            return

        self.list_of_kinds.append(name)
        temp_name = '%s_data' % name
        self.Dict_for_data[temp_name] = []
        temp_name = '%s_index' % name
        self.Dict_for_data[temp_name] = []

    def addData(self, name, data):
        if name not in self.list_of_kinds:
            print("There is no such kind")
            return

        temp_name = '%s_data' % name
        self.Dict_for_data[temp_name].append(data)
        temp_index = len(self.Dict_for_data[temp_name])
        temp_name = '%s_index' % name
        self.Dict_for_data[temp_name].append(temp_index)
        if temp_index > self.borders_for_plot[1]:
            self.borders_for_plot[1] = temp_index
        if data > self.borders_for_plot[3]:
            self.borders_for_plot[3] = data
        elif data < self.borders_for_plot[2]:
            self.borders_for_plot[2] = data


    def showPlot(self):
        for x in range(len(self.list_of_kinds)):
            temp_name = '%s_data' % self.list_of_kinds[x]
            temp_name_index = '%s_index' % self.list_of_kinds[x]
            plt.plot(self.Dict_for_data[temp_name_index], self.Dict_for_data[temp_name],
                     self.KINDS[x],label=self.list_of_kinds[x])
        plt.axis(self.borders_for_plot)
        plt.legend()
        plt.show()

