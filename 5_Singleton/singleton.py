class Singleton(object):
    
    class _Singleton(object):
        pass

    _instance = _Singleton()

    def get_instance(self):
        return self._instance
