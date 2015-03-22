def test_factory():
    from factory import IDCardFactory
    factory = IDCardFactory()
    card = factory.create("John") 
    assert card.use() == "Use the John's card"
