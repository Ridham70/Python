import pytest
from working import convert

def main():
    test_valid_time()
    test_time_with_minutes()
    test_time_without_minutes()
    test_invalid_time()
    test_edge_cases()


def test_valid_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_time_with_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"

def test_time_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

def test_edge_cases():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

    
if __name__ == "__main__":
    main
