from abc import ABCMeta, abstractmethod


class Banner(object):

    def __init__(self, string):
        self.string = string

    def show_with_paren(self):
        return "(" + self.string + ")"

    def show_with_aster(self):
        return "*" + self.string + "*"


class Print(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def print_weak(self):
        pass

    @abstractmethod
    def print_strong(self):
        pass


class PrintBanner(Banner, Print):

    def print_weak(self):
        return self.show_with_paren()

    def print_strong(self):
        return self.show_with_aster()


class PrintBannerTransfer(Print):

    def __init__(self, string):
        self.banner = Banner(string)

    def print_weak(self):
        return self.banner.show_with_paren()

    def print_strong(self):
        return self.banner.show_with_aster()
