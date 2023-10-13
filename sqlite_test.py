##CRUD OPERATIONS IN SQL
import sqlite3

connection=sqlite3.connect('hair-products.db')

cursor=connection.cursor()  

cursor.execute(''' CREATE TABLE IF NOT EXISTS Products
               (product_id INTEGER PRIMARY KEY AUTOINCREMENT, product TEXT,
               supplier TEXT, prices INT)

                ''')
productsToInsert=[
    ('Virgin hair', 'Dangote', 3000),
    ('StraightBone', 'Lush hair', 25000),
    ('Curlyhair', 'Expression', 4000)
]

# cursor.executemany("""
#                INSERT INTO Products(product, supplier, prices)
#                VALUES (?,?,?)
               
#                """, productsToInsert)

cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())


price=(25000,)
cursor.execute("SELECT * FROM Products WHERE prices=?", price)
print(cursor.fetchall())

Estahair_price=(3000,)

cursor.execute("UPDATE Products SET supplier = 'Estaahair' WHERE prices=?", Estahair_price)
print(cursor.fetchall())

cursor.execute("SELECT supplier FROM Products")
print(cursor.fetchall())


cursor.execute("DELETE FROM Products WHERE product_id=3")

cursor.execute("SELECT * FROM Products")
print(cursor.fetchall())

connection.commit()
connection.close()