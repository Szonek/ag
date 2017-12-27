import time


class Event:
    def __init__(self, func_name, iterations = -1):
        self.func_name = func_name
        self.iterations = iterations
        self.elapsed_time_seconds = 0
        self.elapsed_time_miliseconds = 0
        self.start_time = 0
        self.end_time = 0
        self.percent_of_total_execution = 0
        self.result = 0
        pass

    def start(self):
        self.start_time = time.time()
        pass

    def add_result(self, result):
        self.result = result
        pass

    def stop(self):
        self.end_time = time.time()
        self.elapsed_time_seconds = self.end_time - self.start_time
        self.elapsed_time_miliseconds = self.elapsed_time_seconds*1000
        pass


class Profiling:
    def __init__(self, alg_name, arr_events=[]):
        self.alg_name = alg_name
        self.events = arr_events
        self.size = len(self.events)
        self.total_time = sum(x.elapsed_time_seconds for x in self.events)
        self.__update_percentage_of_exec()
        pass

    def add_event(self, event):
        self.events.append(event)
        self.size += 1
        self.total_time += event.elapsed_time_seconds
        self.__update_percentage_of_exec()
        pass

    def __get_key_result(self, e):
        return e.result

    def __gey_key_unique_by_name(self, e):
        if e.func_name == name:
            return e.result
        return -1

    def print_table(self, names):
        self.events.sort(key=self.__get_key_result, reverse=True)
        best_events = []
        for name in names:
            best_events.append(next((x for x in self.events if x.func_name == name), None))

        self.__print_first_row()
        for i, event in enumerate(best_events):
            self.__print_row(i, event)
        pass

    def print_total_table(self):
        self.events.sort(key=self.__get_key_result, reverse=True)
        self.__print_first_row()
        for i, event in enumerate(self.events):
            self.__print_row(i, event)
        pass

    def __update_percentage_of_exec(self):
        for event in self.events:
            event.percent_of_total_execution = event.elapsed_time_seconds / self.total_time
        pass

    def __print_row(self, i, e):
        print('%-5s%-12s%-12s%-12s%-12f%-0.2f' % (str(i) + ".", e.func_name,
                                                  str(e.iterations),
                                                  str(round(e.result,3)),
                                        e.elapsed_time_seconds,
                                        e.percent_of_total_execution))
        pass

    def __print_first_row(self):
        print("--- " + self.alg_name + " ---")
        print('%-5s%-12s%-12s%-12s%-12s%-8s' % ("No.", "Func name", "Iterations", "Result", "Time", "Total[1/100%]"))
        pass
