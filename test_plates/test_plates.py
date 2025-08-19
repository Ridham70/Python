import pytest
from plates import is_valid

def main():
    test_length()
    test_first_two()
    test_space()
    test_not_in_middle()
    test_first_not_zero()

def test_length():
    assert is_valid("HELLO") == True
    assert is_valid("C") == False

def test_first_two():
    assert is_valid("CS") == True
    assert is_valid("50") == False
    assert is_valid("WR") == True

def test_space():
    assert is_valid("PI3.14") == False
    assert is_valid("HI, CS50") == False

def test_not_in_middle():
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True
    assert is_valid("WR03X") == False

def test_first_not_zero():
    assert is_valid("CS05") == False
    assert is_valid("WR01") == False
    assert is_valid("HE88") == True
