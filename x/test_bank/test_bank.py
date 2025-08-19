import pytest
from bank import value

def main():
    test_hello()
    test_startwh()
    test_other()

def test_hello():
    assert value("Hello") == 0
    assert value("Hello, David") == 0
    assert value("hello") == 0
    assert value("hello, Morgan") == 0

def test_startwh():
    assert value("Hey, Morgan") == 20
    assert value("Hi, Alex") == 20

def test_other():
    assert value("Morning, Chris") == 100
    assert value("Good Day, Marco") == 100

if __name__ == "__main__":
    main()

