def test_display():
    """
    >>> from bridge import Display, StringDisplayImpl
    >>> d = Display(StringDisplayImpl("Hello"))
    >>> d.display()
    *******
    *Hello*
    *******
    """


def test_Countdisplay():
    """
    >>> from bridge import CountDisplay, StringDisplayImpl
    >>> d = CountDisplay(StringDisplayImpl("Hello"))

    >>> d.display()
    *******
    *Hello*
    *******

    >>> d.multi_display(2)
    *******
    *Hello*
    *Hello*
    *******
    """
