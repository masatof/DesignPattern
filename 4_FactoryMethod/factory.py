from abc import ABCMeta, abstractmethod


class Product(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def use(self):
        pass


class Factory(object):
    __metaclass__ = ABCMeta

    def create(self, owner):
        p = self._create_product(owner)
        self._register_product(p)
        return p

    @abstractmethod
    def _create_product(self, owner):
        pass

    @abstractmethod
    def _register_product(self, product):
        pass


class IDCard(Product):

    def __init__(self, owner):
        self.owner = owner

    def use(self):
        return "Use the " + self.owner + "'s card"

    def get_owner(self):
        return self.owner


class IDCardFactory(Factory):

    _owners = []

    def _create_product(self, owner):
        return IDCard(owner)

    def _register_product(self, product):
        self._owners.append(product.get_owner())

    def get_owners(self):
        return self._owners
