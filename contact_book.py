import sqlite3

# Connect to database (creates the file if it doesn't exist)
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
)
""")
conn.commit()

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    print("Contact added successfully!\n")

def view_contacts():
    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    if not rows:
        print("No contacts found.\n")
    else:
        print("\n--- Your Contacts ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")
        print()

def search_contact():
    name = input("Enter name to search: ")
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    if not rows:
        print("No matching contacts found.\n")
    else:
        print("\n--- Search Results ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]} | Email: {row[3]}")
        print()

def main():
    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
    conn.close()
