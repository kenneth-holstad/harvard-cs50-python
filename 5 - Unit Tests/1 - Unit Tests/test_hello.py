from hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    assert hello("David") == "hello, David" # to check a single case
    for name in ["Hermione", "Harry", "Ron"]: # to check a whole list
        assert hello(name) == f"hello, {name}"