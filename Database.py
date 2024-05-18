import mysql.connector

def DatabaseCreate():
    cnx = mysql.connector.connect(user='root', password='hello123', host='localhost')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS Inventory")
    Cursor.execute("")
    Cursor.close()
    cnx.close()


def TablesCreate():
    cnx = mysql.connector.connect(user='root', password='hello123', host='localhost', database='Inventory')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS Purchases(ProductCode int(2) Primary Key, ProductName varchar(20),Purchase_Quantity int(3), PurchaseDate Date, PurchasePrice int(3))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Sales(ProductCode int(2) Primary Key,Sale_Quantity int(3), SalesDate Date, SalesPrice int(3))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Inventory(ProductCode int(2) Primary Key, ProductName varchar(20), Quantity int(3),Profit int(3))")
    Cursor.close()
    cnx.close()
