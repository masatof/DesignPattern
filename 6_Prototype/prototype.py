from abc import ABCMeta, abstractmethod


class Product(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def use(self, string):
        pass

    def create_clone(self):
        return self


class Manager(object):

    def __init__(self):
        self.showcase = {}

    def register(self, name, proto):
        self.showcase[name] = proto

    def create(self, protoname):
        return self.showcase.get(protoname).create_clone()


class MessageBox(Product):

    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, string):
        length = len(string)
        result = self.decochar * (length + 4) + "\n"
        result += self.decochar + " " + string + " " + self.decochar + "\n"
        result += self.decochar * (length + 4) + "\n"
        return result
