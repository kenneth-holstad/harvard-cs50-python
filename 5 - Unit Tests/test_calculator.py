'''
before learning assert you could do the opposite by checking for falsehoods:

from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()

'''

import pytest

from calculator import square

'''
# Simpler usage of pytest

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    # you could also test for a specific exception i.e. non-number input with pytest
'''

# split into more clear categories of test cases
# not only does this help categorize what broke, it also allows more tests to run
# because if you run them all in one function 
# then only that one function will tell you it broke once the first one breaks
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError): # tests input line
        square("cat")