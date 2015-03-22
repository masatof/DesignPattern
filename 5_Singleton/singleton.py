class _Singleton(object):
    pass


class Singleton(object):

    _instance = _Singleton()

    def get_instance(self):
        return self._instance
