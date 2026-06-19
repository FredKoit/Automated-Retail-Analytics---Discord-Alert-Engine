import sqlite3
from datetime import datetime

# 1. Connect to the database
conn = sqlite3.connect('company_sales.db')
cursor = conn.cursor()

# 2. Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        category TEXT,
        price REAL,
        quantity INTEGER,
        sale_date TEXT
    )
''')

# 3. Dummy data to simulate a week of company transactions
mock_sales = [
    ('Wireless Mouse', 'Electronics', 25.99, 2, '2026-06-12'),
    ('Mechanical Keyboard', 'Electronics', 89.99, 1, '2026-06-12'),
    ('Ergonomic Chair', 'Furniture', 199.99, 1, '2026-06-13'),
    ('USB-C Hub', 'Electronics', 34.99, 5, '2026-06-14'),
    ('Coffee Mug', 'Kitchen', 12.50, 3, '2026-06-15'),
    ('Desk Mat', 'Office', 18.00, 2, '2026-06-15'),
    ('Noise Cancelling Headphones', 'Electronics', 149.99, 1, '2026-06-16'),
    ('Standing Desk', 'Furniture', 349.99, 1, '2026-06-17'),
]

# 4. Insert the data into the table
cursor.executemany('''
    INSERT INTO sales (product_name, category, price, quantity, sale_date)
    VALUES (?, ?, ?, ?, ?)
''', mock_sales)

# 5. Commit changes and close the connection
conn.commit()
conn.close()

print("Database created and populated successfully!")