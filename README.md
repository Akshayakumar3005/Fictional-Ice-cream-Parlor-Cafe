# Fictional Ice Cream Parlour Cafe

The **Ice Cream Parlor Management System** is a simple, user-friendly application designed to make running an ice cream cafe smoother and more enjoyable for both owners and customers. Using Python and an SQLite database, it helps the parlor manage everything from seasonal flavors and ingredients to customer feedback and allergy concerns.

The application supports two types of users:


Owners
- Add and update seasonal flavors with details like name, description, price, and availability.
- Monitor and update ingredient stock levels to ensure the inventory is sufficient.
- Review customer suggestions for new flavors and address allergy-related feedback.
- Maintain and update a list of allergens to ensure the safety of all customers.
Customers
- Browse the menu to view available flavors and search by name or seasonal availability.
- Suggest new flavors to the owner, including notes about potential allergens.
- Add desired flavors to a shopping cart, update quantities, and proceed with their purchase.

## Tech Stack

**Programming Language:** Python

**Database:** SQLite

**Backend Library:** SQLite3 Library

**Deployment Environment:** Docker
## Python Installation

- Ensure you have python in your system. For windows users download it from https://www.python.org/downloads/.  For Mac users download it from Homebrew.
  ```bash
    brew install python
  ```

- You can check if Python is installed on your system and verify its version by running the following command
  ```bash
    python --version
  ```
## Run Locally

Clone the project

```bash
  git clone https://github.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe
```

Click '**Windows button + R** to open the command prompt in Windows OS' or 'Go to Application -> utilities -> terminal in Mac OS' and go to the project directory 

```bash
  cd "lt hackton"
```

Run the main.py file

```bash
  python3 main.py
```

## To run from Docker

```bash
  docker built -t myapp .
  docker run myapp
```

## Screenshots
Owner Side:
 So intiallly,
- This displays the WELCOME prompt which has two separate options as "OWNER" and "CUSTOMER"
- Lets the owner apply "search and filter"!
- It lets search by either its name or season or both
- Lets the owner update the quantity of the ingredient!
- It asks for the name of the ingredient to update, its quantity to add or subtract, the +/- operation
- Lets the owner view the suggestions posted by the customers!
- Lets the owner alert the customer about any allergic ingredient that might be present in the ice cream!
(Substances like milk and nuts are allergic to some)
- Lets the owner view the list of allergens!
- This helps them verify and add new allergens, if any Lets the owner EXIT the application

![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/welcoem.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/add.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/addallergen.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/addingr.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/exit.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/menu.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/search.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/serach.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/updteingri.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/view.jpeg)
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/screenshotsOwneroutput/viewalergi.jpeg)

Customer Side:
It work based on:
(i) This displays the WELCOME prompt which has two separate options as "OWNER" and "CUSTOMER"
(ii) Main menu for Customer
(iii) option 1 : Lets the customer apply "search and filter"!
- It lets search by either its name or just a part of it or season or both
- Displays all relevant options irrespective of case (case-insensitive)
- Lets the customer add suggestions like toppings or allergy conc
- When the customer enters an irrelevant word or unavailable flavours to search, it displays this output
- Lets the customer view the available flavours, description and their prices (like a menu) and lets them pick their required quantity!
- Lets the customer view the items in the cart to confirm once before ordering!
- Shows the cumulative price of each item as well as the total amount
- Lets the customer remove items from cart
- Lets the customer EXIT the application
![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/ScreenshootCustomer/serach.jpeg)

![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/ScreenshootCustomer/search.jpeg)

![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/ScreenshootCustomer/add.jpeg)

![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/ScreenshootCustomer/addcart.jpeg)

![App Screenshot](https://raw.githubusercontent.com/Akshayakumar3005/Fictional-Ice-cream-Parlor-Cafe/refs/heads/main/lt%20hackton/ScreenshootCustomer/viewcart.jpeg)
