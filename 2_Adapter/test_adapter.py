def test_adapter_extend():
    from adapter import PrintBanner
    p = PrintBanner("Hello")
    assert p.print_weak() == "(Hello)"
    assert p.print_strong() == "*Hello*"


def test_adapter_transfer():
    from adapter import PrintBannerTransfer
    p = PrintBannerTransfer("Hello")
    assert p.print_weak() == "(Hello)"
    assert p.print_strong() == "*Hello*"
