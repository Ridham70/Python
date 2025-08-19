import pytest
from twttr import shorten


def main():
    test_vowel()
    test_notvowel()
    test_num()

def test_vowel():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("Orange") == "rng"
    assert shorten("What's your name? ") == "Wht's yr nm? "


def test_notvowel():
    assert shorten("Cyst") == "Cyst"
    assert shorten("Rhytham") == "Rhythm"

def test_num():
    assert shorten("CS50P") == "CS50P"


if __name__ == "__main__":
    main()


