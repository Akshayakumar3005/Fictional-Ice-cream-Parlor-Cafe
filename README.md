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

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)
