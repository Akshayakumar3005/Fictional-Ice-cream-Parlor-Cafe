import sqlite3
import datetime

DB_NAME = "ice_cream_parlor.db"

def db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row 
    return conn

def initialize_db():
    conn = db_connection()
    cursor = conn.cursor()

    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL,
        available INTEGER DEFAULT 1,
        season TEXT
    );

    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        quantity REAL NOT NULL,
        unit TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS customer_suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        flavor_name TEXT NOT NULL,
        suggestion_date TEXT NOT NULL,
        allergy_concerns TEXT
    );

    CREATE TABLE IF NOT EXISTS allergens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (flavor_id) REFERENCES seasonal_flavors (id)
    );
    """)
    conn.commit()
    conn.close()

initialize_db()

def add_flavor(name, description, price, season):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO seasonal_flavors (name, description, price, season)
        VALUES (?, ?, ?, ?)
    """, (name, description, price, season))
    conn.commit()
    conn.close()
    print(f"Flavor '{name}' added successfully.")

def search_flavors(search_term=None, filter_season=None):
    conn = db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM seasonal_flavors WHERE 1"
    params = []

    if search_term:
        query += " AND name LIKE ?"
        params.append(f"%{search_term}%")
    if filter_season:
        query += " AND season = ?"
        params.append(filter_season)

    cursor.execute(query, params)
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(f"Name: {row['name']}, Description: {row['description']}, Price: {row['price']}, Season: {row['season']}")
    else:
        print("No flavors found.")

    conn.close()

def add_ingredient(name, quantity, unit):
    conn = db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO ingredients (name, quantity, unit)
            VALUES (?, ?, ?)
        """, (name, quantity, unit))
        conn.commit()
        print(f"Ingredient '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Ingredient '{name}' already exists.")
    conn.close()

def add_customer_suggestion(customer_name, flavor_name, allergy_concerns=None):
    suggestion_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO customer_suggestions (customer_name, flavor_name, suggestion_date, allergy_concerns)
        VALUES (?, ?, ?, ?)
    """, (customer_name, flavor_name, suggestion_date, allergy_concerns))
    conn.commit()
    conn.close()
    print(f"Suggestion from {customer_name} for flavor '{flavor_name}' added successfully.")

def view_customer_suggestions():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer_suggestions")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"Customer: {row['customer_name']}, Flavor: {row['flavor_name']}, Date: {row['suggestion_date']}, Allergy Concerns: {row['allergy_concerns']}")
    else:
        print("No customer suggestions found.")
    conn.close()

def add_allergen(name):
    conn = db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO allergens (name)
            VALUES (?)
        """, (name,))
        conn.commit()
        print(f"Allergen '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Allergen '{name}' already exists.")
    conn.close()

def view_allergens():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM allergens")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"Allergen: {row['name']}")
    else:
        print("No allergens found.")
    conn.close()

def add_to_cart():
    conn = db_connection()
    cursor = conn.cursor()

    # Display all available flavors with details
    cursor.execute("SELECT * FROM seasonal_flavors WHERE available = 1")
    rows = cursor.fetchall()

    if rows:
        print("\nAvailable Flavors:")
        for row in rows:
            print(f"ID: {row['id']}\nFlavor: {row['name']}\nDescription: {row['description']}\nPrice: ${row['price']:.2f}\n")
            
        # Prompt the user for flavor ID and quantity
        flavor_id = int(input("Enter the Flavor ID you want to add to the cart: "))
        quantity = int(input("Enter the quantity: "))
        try:
            # Verify the selected flavor exists and is available
            cursor.execute("SELECT * FROM seasonal_flavors WHERE id = ? AND available = 1", (flavor_id,))
            flavor = cursor.fetchone()
            if flavor:
                # Add the flavor to the cart
                cursor.execute("""
                    INSERT INTO cart (flavor_id, quantity)
                    VALUES (?, ?)
                """, (flavor_id, quantity))
                conn.commit()
                print(f"Added {quantity} of '{flavor['name']}' to the cart.")
            else:
                print("Invalid Flavor ID or flavor is not available.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    else:
        print("No flavors are currently available.")

    conn.close()

    
def view_cart():
    conn = db_connection()
    cursor = conn.cursor()
    
    # Query to get cart details including price and quantity
    cursor.execute("""
        SELECT c.id, s.name, c.quantity, s.price, (c.quantity * s.price) AS total_price
        FROM cart c
        JOIN seasonal_flavors s ON c.flavor_id = s.id
    """)
    rows = cursor.fetchall()
    if rows:
        grand_total = 0  # To keep track of the total cost of the cart
        print("\nCart Details:")
        for row in rows:
            print(f"Cart ID: {row['id']}, Flavor: {row['name']}, Quantity: {row['quantity']}, Price per unit: ${row['price']:.2f}, Total: ${row['total_price']:.2f}")
            grand_total += row['total_price']  # Accumulate the total price
        
        print(f"\nGrand Total: ${grand_total:.2f}")
    else:
        print("Your cart is empty.")
    
    conn.close()


def remove_from_cart(cart_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cart WHERE id = ?", (cart_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Item with Cart ID {cart_id} removed from cart.")
    else:
        print(f"Item with Cart ID {cart_id} not found.")
    conn.close()


def update_ingredient_quantity(name, quantity, operation):
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM ingredients WHERE name = ?", (name,))
    row = cursor.fetchone()

    if row:
        current_quantity = row['quantity']

        if operation == 'add':
            new_quantity = current_quantity + quantity
        elif operation == 'subtract':
            if current_quantity >= quantity:
                new_quantity = current_quantity - quantity
            else:
                print(f"Cannot subtract {quantity} from {name}, insufficient stock.")
                conn.close()
                return
        else:
            print("Invalid operation. Use 'add' or 'subtract'.")
            conn.close()
            return

        cursor.execute("""
            UPDATE ingredients
            SET quantity = ?
            WHERE name = ?
        """, (new_quantity, name))
        conn.commit()
        print(f"Updated '{name}' quantity to {new_quantity}.")
    else:
        print(f"Ingredient '{name}' does not exist in the database.")

    conn.close()

def main_menu():
    print("\nWelcome to the Ice Cream Parlor Management System!")
    user_role = input("Are you an 'Owner' or a 'Customer'? ").strip().lower()

    if user_role not in ['owner', 'customer']:
        print("Invalid role. Please restart and choose either 'Owner' or 'Customer'.")
        return

    while True:
        print("\nMain Menu:")

        if user_role == 'owner':
            print("1. Add New Flavor")
            print("2. Search & Filter Flavors")
            print("3. Add Ingredient")
            print("4. Update Ingredient Quantity")
            print("5. View Customer Suggestions")
            print("6. Add Allergen")
            print("7. View Allergen List")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ").strip()

            if choice == '1':
                name = input("Enter flavor name: ").strip()
                description = input("Enter flavor description: ").strip()
                price = float(input("Enter price: ").strip())
                season = input("Enter season: ").strip()
                add_flavor(name, description, price, season)
            elif choice == '2':
                search_term = input("Enter search term (or press Enter to skip): ").strip()
                filter_season = input("Enter season to filter by (or press Enter to skip): ").strip()
                search_flavors(search_term, filter_season)
            elif choice == '3':
                name = input("Enter ingredient name: ").strip()
                quantity = float(input("Enter quantity: ").strip())
                unit = input("Enter unit (e.g., kg, liters): ").strip()
                add_ingredient(name, quantity, unit)
            elif choice == '4':
                name = input("Enter ingredient name to update: ").strip()
                quantity = float(input("Enter quantity to add/subtract: ").strip())
                operation = input("Enter operation ('add' or 'subtract'): ").strip().lower()
                update_ingredient_quantity(name, quantity, operation)
            elif choice == '5':
                view_customer_suggestions()
            elif choice == '6':
                allergen_name = input("Enter allergen name to add: ").strip()
                add_allergen(allergen_name)
            elif choice == '7':
                view_allergens()
            elif choice == '8':
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        elif user_role == 'customer':
            print("1. Search & Filter Flavors")
            print("2. Add Customer Suggestion")
            print("3. Add to Cart")
            print("4. View Cart")
            print("5. Remove from Cart")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == '1':
                search_term = input("Enter search term (or press Enter to skip): ").strip()
                filter_season = input("Enter season to filter by (or press Enter to skip): ").strip()
                search_flavors(search_term, filter_season)
            elif choice == '2':
                customer_name = input("Enter your name: ").strip()
                flavor_name = input("Enter flavor name suggestion: ").strip()
                allergy_concerns = input("Enter any allergy concerns (or press Enter to skip): ").strip()
                add_customer_suggestion(customer_name, flavor_name, allergy_concerns)
            elif choice == '3':
                add_to_cart()
            elif choice == '4':
                view_cart()
            elif choice == '5':
                cart_id = int(input("Enter Cart ID to remove: ").strip())
                remove_from_cart(cart_id)
            
            elif choice == '6':
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
main_menu()