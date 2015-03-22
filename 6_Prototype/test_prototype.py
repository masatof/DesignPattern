def test_prototype():
    from prototype import Manager, MessageBox
    manager = Manager()
    manager.register("warning box", MessageBox('*'))

    product = manager.create("warning box")
    expected = "*****************\n"
    expected += "* Hello, world. *\n"
    expected += "*****************\n"
    assert product.use("Hello, world.") == expected
