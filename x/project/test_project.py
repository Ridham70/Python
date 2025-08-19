from project import get_menu, select_menu, open_selected_menu, get_username, get_mobile_number, print_receipt, generate_invoice_pdf
from unittest.mock import mock_open, patch
import pytest, os
import tempfile

def main():
    test_get_username()
    test_get_mobile_number()
    test_get_menu()
    test_select_menu()
    test_open_selected_menu()

    with tempfile.TemporaryDirectory() as tmpdir:
        test_generate_invoice_pdf(tmpdir)

def test_get_username():
    # Mock the input function to return the desired test username
    valid_names = ["John Doe", "Ms. Jane Smith", "Dr. John-Paul", "Alice"]
    invalid_then_valid_cases = [
        (["J@ne", "John Doe"], "John Doe"),
        (["123", "Alice"], "Alice"),
        (["Mr.John", "Ms. Jane Smith"], "Ms. Jane Smith"),
        (["Mr. John123", "Dr. John-Paul"], "Dr. John-Paul"),
    ]

    for x in valid_names:
        with patch('builtins.input', return_value=x):
            username = get_username()
            assert username == x
    for inputs, expected in invalid_then_valid_cases:
        with patch('builtins.input', side_effect=inputs):
            username = get_username()
            assert username == expected

def test_get_mobile_number():
    valid_numbers = ["9876543210", "1234567890", "9999999999"]

    # Valid inputs should return directly
    for number in valid_numbers:
        with patch('builtins.input', return_value=number), patch('builtins.print') as mock_print:
            assert get_mobile_number() == number
            mock_print.assert_not_called()

    # Invalid → valid input test cases
    invalid_then_valid_cases = [
        (["12345", "9876543210"], "9876543210"),
        (["abcdefghij", "1234567890"], "1234567890"),
        (["12345678901", "9999999999"], "9999999999"),
        (["98765abc10", "8888888888"], "8888888888"),
    ]

    expected_error_msg = "Invalid mobile number. Please enter exactly 10 digits."

    for inputs, expected in invalid_then_valid_cases:
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mock_print:
            assert get_mobile_number() == expected
            mock_print.assert_any_call(expected_error_msg)

def test_get_menu():
    mock_csv_data = "id,submenu\n1,bakery\n2,dairy\n3,drinks\n4,fruits\n5,meat\n6,vegetable"

    # Expected output from csv.DictReader
    expected_result = [
        {'id': '1', 'submenu': 'bakery'},
        {'id': '2', 'submenu': 'dairy'},
        {'id': '3', 'submenu': 'drinks'},
        {'id': '4', 'submenu': 'fruits'},
        {'id': '5', 'submenu': 'meat'},
        {'id': '6', 'submenu': 'vegetable'}
    ]

    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = get_menu()
        assert result == expected_result

def test_select_menu():
    menu_list = [
        {'id': '1', 'submenu': 'bakery'},
        {'id': '2', 'submenu': 'dairy'},
        {'id': '3', 'submenu': 'drinks'},
        {'id': '4', 'submenu': 'fruits'},
        {'id': '5', 'submenu': 'meat'},
        {'id': '6', 'submenu': 'vegetable'}
    ]

    # Case 1: Valid input (3 → "drinks")
    with patch("builtins.input", return_value="3"):
        assert select_menu(menu_list) == "drinks"

    # Case 2: User enters 0 → should return "done"
    with patch("builtins.input", return_value="0"):
        assert select_menu(menu_list) == "done"

    # Case 3: Out-of-range number (10) → then valid input (5 → "meat")
    with patch("builtins.input", side_effect=["10", "5"]), patch("builtins.print") as mock_print:
        assert select_menu(menu_list) == "meat"
        mock_print.assert_any_call("Invalid selection. Please try again.")

    # Case 4: Non-numeric input ("xyz") → then valid input (6 → "vegetable")
    with patch("builtins.input", side_effect=["xyz", "6"]), patch("builtins.print") as mock_print:
        assert select_menu(menu_list) == "vegetable"
        mock_print.assert_any_call("Invalid input. Please enter a number.")

def test_open_selected_menu():
    submenu_files = {
        "bakery": """ItemID,ItemName,Price
1,Whole Wheat Bread,40
2,Croissant,25
3,Chocolate Cake,220
4,Buns,35""",
        "dairy": """ItemID,ItemName,Price
1,Milk,60
2,Cheddar Cheese,150
3,Yogurt,50
4,Eggs,70""",
        "drinks": """ItemID,ItemName,Price
1,Coca-Cola,60
2,Orange Juice,90
3,Green Tea,20
4,Packaged Water,20""",
        "fruits": """ItemID,ItemName,Price
1,Apple,120
2,Banana,40
3,Mango,150
4,Orange,80
5,Papaya,45""",
        "meat": """ItemID,ItemName,Price
1,Chicken Breast,250
2,Salmon,800
3,Mutton,600
4,Prawns,700""",
        "vegetable": """ItemID,ItemName,Price
1,Tomato,25
2,Spinach,30
3,Potato,20
4,Carrot,40
5,Cauliflower,35"""
    }

    for submenu, csv_data in submenu_files.items():
        expected = [
            dict(zip(["ItemID", "ItemName", "Price"], line.split(',')))
            for line in csv_data.strip().split('\n')[1:]
        ]

        with patch("builtins.open", mock_open(read_data=csv_data)):
            with patch("builtins.print") as mock_print:
                result = open_selected_menu(submenu)
                assert result == expected
                mock_print.assert_any_call("\nAvailable Items:")
                for item in expected:
                    mock_print.assert_any_call(f"{item['ItemID']}, {item['ItemName']}, {item['Price']}")

def test_print_receipt():
    username = "John Doe"
    mobile_number = "9876543210"
    cart = [
        {'ItemID': '1', 'ItemName': 'Apple', 'Price': 120.0, 'Quantity': 2},
        {'ItemID': '2', 'ItemName': 'Banana', 'Price': 40.0, 'Quantity': 3}
    ]

    # Expected total: (120 * 2) + (40 * 3) = 240 + 120 = 360
    expected_lines = [
        "\n--- YOUR RECEIPT ---",
        f"Name: {username}",
        f"Mobile: {mobile_number}",
        "QUANTITY  ITEM         PRICE     AMOUNT",
        "------------------------------------------",
        "2        Apple       $120.00  $240.00  ",
        "3        Banana      $40.00   $120.00  ",
        "------------------------------------------",
        "Total Amount: $360.00"
    ]

    with patch("builtins.print") as mock_print:
        print_receipt(username, mobile_number, cart)

        # Flatten all printed lines into a list of strings
        printed_lines = [args[0] for args, _ in mock_print.call_args_list]

        for line in expected_lines:
            assert any(line in printed for printed in printed_lines), f"Missing: {line}"

def test_generate_invoice_pdf(tmp_path):
    username = "JohnDoe"
    mobile_number = "9876543210"
    cart = [
        {'ItemID': '1', 'ItemName': 'Apple', 'Price': 100.0, 'Quantity': 2},  # $200
        {'ItemID': '2', 'ItemName': 'Banana', 'Price': 50.0, 'Quantity': 1}   # $50
    ]

    # Expected file name
    expected_file = f"{username}_{mobile_number}_invoice.pdf"
    expected_path = tmp_path / expected_file

    # Patch the working directory to temporary path
    original_cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        generate_invoice_pdf(username, mobile_number, cart)

        # Check file exists
        assert expected_path.exists(), "Invoice PDF was not generated."

        # Check file is not empty
        assert expected_path.stat().st_size > 0, "Generated PDF is empty."
    finally:
        os.chdir(original_cwd)


if __name__ == "__main__":
    main()

