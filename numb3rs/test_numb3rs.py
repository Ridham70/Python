import pytest
from numb3rs import validate

def main():
    test_format()
    test_range()
    test_notanumber()

def test_format():
    assert validate("10.1.1.1") == True
    assert validate("255.255.255.0") == True
    assert validate("10.1.1") == False
    assert validate("10.1") == False
    assert validate("10") == False

def test_range():
    assert validate("255.255.255.255") == True
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False

def test_notanumber():
    assert validate("cat.cat.cat.cat") == False
    assert validate("10.1.1.1") == True

if __name__ == "__main__":
    main()





