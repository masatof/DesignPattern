def test_char_display():
    from template import CharDisplay
    assert CharDisplay("H").display() == "<<HHHHH>>"


def test_string_display():
    from template import StringDisplay
    expected = "+-----+\n"
    expected += "|Hello|\n" * 5
    expected += "+-----+\n"
    assert StringDisplay("Hello").display() == expected
