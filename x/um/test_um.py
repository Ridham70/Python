import pytest
from um import count

def main():
    test_case_insensitive()
    test_substring()
    test_valid()

def test_case_insensitive() :
    assert count("Um, thanks for the album.") == 1
    assert count("Um, hello, um, world ") == 2

def test_substring():
    assert count("hello") == 0
    assert count("yummy") == 0

def test_valid():
    assert count("hello, um, world") == 1
    assert count("um..") == 1

if __name__ == "__main__":
    main()
