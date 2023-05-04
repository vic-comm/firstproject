import pytest
"""def main():
    x = int(input("what's x \n"))
    print("x squared is", square(x))


def square(v):
    return pow(v, 2)
    # return v + 2


def test_square():
    assert square(2) == 4


def test_negative():
    assert square(-6) == 36
    assert square(-14) == 196


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == '__main__':
    main()"""

def main():
    name = input("What's your name")
    print(hello(name))


def hello(x='World'):
    return f"Hello {x}"


def test_hello():
    assert hello('victor') == 'Hello victor'




