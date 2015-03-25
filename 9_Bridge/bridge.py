from abc import ABCMeta, abstractmethod


class Display(object):

    def __init__(self, impl):
        self._impl = impl

    def open(self):
        self._impl.raw_open()

    def printdata(self):
        self._impl.raw_print()

    def close(self):
        self._impl.raw_close()

    def display(self):
        self.open()
        self.printdata()
        self.close()


class CountDisplay(Display):

    def multi_display(self, times):
        self.open()
        for _ in range(times):
            self.printdata()
        self.close()


class DisplayImpl(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass


class StringDisplayImpl(DisplayImpl):

    def __init__(self, string):
        self._string = string

    def raw_open(self):
        self._print_line()

    def raw_print(self):
        print "*" + self._string + "*"

    def raw_close(self):
        self._print_line()

    def _print_line(self):
        print '*' * (len(self._string) + 2)
