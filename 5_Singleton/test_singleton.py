def test_singleton():
    from singleton import Singleton
    obj1 = Singleton().get_instance()
    obj2 = Singleton().get_instance()
    assert obj1 == obj2
