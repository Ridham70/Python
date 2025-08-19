import csv
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def main():
    # Get user information
    username = get_username()
    mobile_number = get_mobile_number()

    # Initialize cart
    cart = []

    while True:
        # Get menu and select submenu
        menu = get_menu()
        selected_submenu = select_menu(menu)

        if selected_submenu == "done":
            break

        if selected_submenu == "Invalid selection.":
            print("Invalid menu selection. Exiting.")
            break

        # Open selected submenu and display items
        items = open_selected_menu(selected_submenu)
        if not items:
            print("No items available in the selected submenu.")
            continue

        # Add item to cart
        while True:
            selected_item_id = input("\nEnter item ID to add to the cart (or 'done' to finish adding from this menu): ").strip()
            if selected_item_id.lower() == 'done':
                break

            quantity = input("How many items do you want to add? ")
            if not quantity.isdigit() or int(quantity) <= 0:
                print("Invalid quantity. Please enter a positive integer.")
                continue

            quantity = int(quantity)
            item_found = False

            for item in items:
                if item['ItemID'] == selected_item_id:
                    cart.append({
                        'ItemID': item['ItemID'],
                        'ItemName': item['ItemName'],
                        'Price': float(item['Price']),
                        'Quantity': quantity
                    })
                    print(f"Added {quantity}x {item['ItemName']} to cart.")
                    item_found = True
                    break

            if not item_found:
                print("Item not found. Please try again.")

        # Ask if user wants to select another submenu
        continue_shopping = input("\nDo you want to select another submenu? (yes/no): ").strip().lower()
        if continue_shopping != 'yes':
            break

    # Print receipt and generate PDF
    if cart:
        print_receipt(username, mobile_number, cart)
        generate_invoice_pdf(username, mobile_number, cart)
    else:
        print("No items in cart. Receipt not generated.")

def generate_invoice_pdf(username, mobile_number, cart):
    file_path = f"{username}_{mobile_number}_invoice.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Draw table
    c.setFont("Helvetica", 10)
    c.drawString(100, height - 50, "INVOICE")
    c.drawString(100, height - 80, f"To: {username}")
    c.drawString(100, height - 100, f"Phone: {mobile_number}")

    c.setFont("Helvetica", 8)
    c.drawString(50, height - 150, "Qty")
    c.drawString(150, height - 150, "Description")
    c.drawString(300, height - 150, "Unit Price")
    c.drawString(400, height - 150, "Line Total")

    total_amount = 0
    for index, item in enumerate(cart):
        amount = item['Price'] * item['Quantity']
        total_amount += amount
        c.drawString(50, height - 180 - index * 20, str(item['Quantity']))
        c.drawString(150, height - 180 - index * 20, item['ItemName'])
        c.drawString(300, height - 180 - index * 20, f"${item['Price']:.2f}")
        c.drawString(400, height - 180 - index * 20, f"${amount:.2f}")

    c.drawString(50, height - 250, "Subtotal")
    c.drawString(400, height - 250, f"${total_amount:.2f}")

    # total
    c.drawString(50, height - 310, "Total")
    c.drawString(400, height - 310, f"${total_amount:.2f}")

    c.save()
    print(f"Invoice generated: {file_path}")

def get_menu():
    with open("menu.csv", "r") as file:
        menu = list(csv.DictReader(file))
    return menu

def select_menu(menu_list):
    for index, item in enumerate(menu_list, start=1):
        print(f"{index}. {item['submenu']}")

    while True:
        try:
            selected_menu = int(input("Enter number to select menu (or 0 to finish shopping): ")) - 1
            if selected_menu == -1:  # User wants to finish shopping
                return "done"
            if 0 <= selected_menu < len(menu_list):
                return menu_list[selected_menu]['submenu']
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def open_selected_menu(selected_menu):
    sm = f"{selected_menu}.csv"
    try:
        with open(sm, "r") as file:
            menu = list(csv.DictReader(file))
            print("\nAvailable Items:")
            for item in menu:
                print(f"{item['ItemID']}, {item['ItemName']}, {item['Price']}")
            return menu
    except FileNotFoundError:
        print(f"The file {sm} was not found.")
        return []

def print_receipt(username, mobile_number, cart):
    print("\n--- YOUR RECEIPT ---")
    print(f"Name: {username}")
    print(f"Mobile: {mobile_number}")
    print("\nQUANTITY  ITEM         PRICE     AMOUNT")
    print("------------------------------------------")

    total_amount = 0
    for item in cart:
        amount = item['Price'] * item['Quantity']
        total_amount += amount
        print(f"{item['Quantity']:<9}{item['ItemName']:<12}${item['Price']:<8.2f}${amount:<8.2f}")

    print("------------------------------------------")
    print(f"Total Amount: ${total_amount:.2f}")

def get_username():
    pattern = r"^(?:Mr\. |Ms\. |Mrs\. |Dr\. )?[A-Za-z]+(?:-[A-Za-z]+)?(?: [A-Za-z]+)?$"
    while True:
        user_input = input("Enter your name: ").strip()
        if re.match(pattern, user_input, re.IGNORECASE):
            return user_input
        print("Invalid name format.")

def get_mobile_number():
    pattern = r"^\d{10}$"
    while True:
        user_input = input("Enter 10-digit mobile number: ").strip()
        if re.match(pattern, user_input):
            return user_input
        print("Invalid mobile number. Please enter exactly 10 digits.")

if __name__ == "__main__":
    main()
