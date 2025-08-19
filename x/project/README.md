# Supermarket Billing System with PDF Invoice

#### Video Demo: <https://youtu.be/6bb7AsmkGhQ?si=KMoSYCVaRa2D42UB>

#### Description:
This is a Python-based console application that simulates a supermarket billing system. It allows the user to:

- Select categories (submenus) such as bakery, dairy, drinks, etc.
- View and choose individual items from each category
- Enter quantity for items
- Add selected items to a cart
- Print a formatted receipt to the terminal
- Generate a professional PDF invoice using the `reportlab` library

The application includes input validation for:
- User's name (supports optional prefixes like Mr., Ms., Dr.)
- Mobile number (must be 10 digits)
- Item selection and quantity

The project also includes a full test suite written using `pytest`. These tests cover:

- User input validation (names and mobile numbers)
- Menu and submenu file loading
- Item selection logic
- Console receipt output
- PDF invoice generation and file verification

The item and category data are managed through CSV files:
- `menu.csv`
- `bakery.csv`, `dairy.csv`, `drinks.csv`, `fruits.csv`, `meat.csv`, `vegetable.csv`

---

#### Requirements:
Install project dependencies using:

```bash
pip install -r requirements.txt

### 📁 CSV Files Used

Below are the CSV files used in this project along with sample data from each:

---

#### `menu.csv`
Contains main menu categories available for selection.

```csv
id,submenu
1,bakery
2,dairy
3,drinks
4,fruits
5,meat
6,vegetable

 #### `bakery.csv`

 Contains Items available under the Bakery category.

 ```csv
 ItemID,ItemName,Price
 1,Whole Wheat Bread,40
 2,Croissant,25
 3,Chocolate Cake,220
 4,Buns,35

  #### `dairy.csv`

  Contains Items available under the Dairy category.

  ```csv
  ItemID,ItemName,Price
  1,Milk,60
  2,Cheddar Cheese,150
  3,Yogurt,50
  4,Eggs,70

   #### `drinks.csv`

   Contains Items available under the Drinks category.

   ```csv
   ItemID,ItemName,Price
   1,Coca-Cola,60
   2,Orange Juice,90
   3,Green Tea,20
   4,Packaged Water,20

    #### `fruits.csv`

    Contains Items available under the Fruits category.

    ```csv
    ItemID,ItemName,Price
    1,Apple,120
    2,Banana,40
    3,Mango,150
    4,Orange,80
    5,Papaya,45

     #### `meat.csv`

     Contains Items available under the Meat category.

     ```csv
     ItemID,ItemName,Price
     1,Chicken Breast,250
     2,Salmon,800
     3,Mutton,600
     4,Prawns,700

      #### `vegetable.csv`

      Contains Items available under the Vegetable category.

      ```csv
      ItemID,ItemName,Price
      1,Tomato,25
      2,Spinach,30
      3,Potato,20
      4,Carrot,40
      5,Cauliflower,35

      #### File Structure:
      project/
      ├── project.py
      ├── test_project.py
      ├── requirements.txt
      ├── README.md
      ├── menu.csv
      ├── bakery.csv
      ├── dairy.csv
      ├── drinks.csv
      ├── fruits.csv
      ├── meat.csv
      ├── vegetable.csv
