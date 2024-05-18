#PYTHON MODULE: PURCHASES
from sys import platform

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform


def clear_screen():
    # Print multiple newlines to simulate clearing the screen
    print("\n" * 100)

def get_connection():
    return mysql.connector.connect(user='root', password='hello123', host='localhost', database='Inventory')

def insert_purchase():
    try:
        clear_screen()
        cnx = get_connection()
        cursor = cnx.cursor()

        product_code = int(input("Enter Product Code: "))
        purchase_quantity = int(input("Enter Purchase Quantity: "))
        purchase_date = input("Enter Purchase Date (YYYY-MM-DD): ")
        purchase_price = int(input("Enter Purchase Price: "))

        query = '''
        INSERT INTO Purchases (ProductCode, Purchase_Quantity, PurchaseDate, PurchasePrice)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(query, (product_code, purchase_quantity, purchase_date, purchase_price))
        cnx.commit()

        update_inventory_purchase(product_code, purchase_quantity)

        print("Purchase record inserted successfully.")
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_inventory_purchase(product_code, purchase_quantity):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        cursor.execute("SELECT Quantity FROM Inventory WHERE ProductCode = %s", (product_code,))
        result = cursor.fetchone()

        if result:
            current_quantity = result[0]
            new_quantity = current_quantity + purchase_quantity
            cursor.execute("UPDATE Inventory SET Quantity = %s WHERE ProductCode = %s", (new_quantity, product_code))
        else:
            product_name = input("Enter Product Name: ")
            cursor.execute("INSERT INTO Inventory (ProductCode, ProductName, Quantity, Profit) VALUES (%s, %s, %s, %s)", (product_code, product_name, purchase_quantity, 0))

        cnx.commit()
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def read_all_purchases():
    try:
        clear_screen()
        cnx = get_connection()
        cursor = cnx.cursor()

        query = "SELECT * FROM Purchases"
        cursor.execute(query)

        for (ProductCode, Purchase_Quantity, PurchaseDate, PurchasePrice) in cursor:
            print("=============================================================")
            print(f"Product Code    : {ProductCode}")
            print(f"Purchase Quantity : {Purchase_Quantity}")
            print(f"Purchase Date   : {PurchaseDate}")
            print(f"Purchase Price  : {PurchasePrice}")
            print("=============================================================")

        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_purchase():
    try:
        clear_screen()
        cnx = get_connection()
        cursor = cnx.cursor()

        product_code = int(input("Enter Product Code to delete: "))

        cursor.execute("DELETE FROM Purchases WHERE ProductCode = %s", (product_code,))
        cnx.commit()

        print("Purchase record deleted successfully.")
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

