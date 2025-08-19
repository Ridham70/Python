import pytest
from datetime import date
from seasons import get_date, date_to_min, min_to_word

def main():
    test_get_date()
    test_date_to_min()
    test_min_to_word()
    test_edge_cases()

def test_get_date(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2000-01-01")
    assert get_date() == date(2000, 1, 1)

    monkeypatch.setattr('builtins.input', lambda _: "1999-01-01")
    assert get_date() == date(1999, 1, 1)

    monkeypatch.setattr('builtins.input', lambda _: "01-01-2000")
    try:
        get_date()
        assert False, "Expected SystemExit"
    except SystemExit:
        assert True

def test_date_to_min():
    assert date_to_min(date(2000, 1, 1)) == 13403520

def test_min_to_word():
    assert min_to_word(0) == "Zero minutes"
    assert min_to_word(1) == "One minutes"
    assert min_to_word(45) == "Forty-five minutes"
    assert min_to_word(100) == "One hundred minutes"
    assert min_to_word(1000) == "One thousand minutes"
    assert min_to_word(1000000) == "One million minutes"

def test_edge_cases():
    assert min_to_word("2799360") == "Two million, seven hundred ninety-nine thousand, three hundred sixty minutes"


