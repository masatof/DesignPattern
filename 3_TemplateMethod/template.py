from abc import ABCMeta, abstractmethod


class AbstractDisplay(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def message(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        result = ""
        result += self.open()
        for _ in range(5):
            result += self.message()
        result += self.close()
        return result


class CharDisplay(AbstractDisplay):

    def __init__(self, ch):
        self.ch = ch

    def open(self):
        return "<<"

    def message(self):
        return self.ch

    def close(self):
        return ">>"


class StringDisplay(AbstractDisplay):

    def __init__(self, string):
        self.string = string

    def open(self):
        return self.print_line()

    def message(self):
        return "|" + self.string + "|\n"

    def close(self):
        return self.print_line()

    def print_line(self):
        return "+" + len(self.string) * '-' + "+\n"
