import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os


def clear_screen():
    # Print multiple newlines to simulate clearing the screen
    print("\n" * 100)

def get_connection():
    return mysql.connector.connect(user='root', password='hello123', host='localhost', database='Inventory')

def insert_inventory():
    try:
        clear_screen()
        cnx = get_connection()
        cursor = cnx.cursor()

        product_code = int(input("Enter Product Code: "))
        product_name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        profit = int(input("Enter Profit: "))

        query = '''
        INSERT INTO Inventory (ProductCode, ProductName, Quantity, Profit)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(query, (product_code, product_name, quantity, profit))
        cnx.commit()

        print("Inventory record inserted successfully.")
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def read_all_inventory():
    try:
        clear_screen()
        cnx = get_connection()
        cursor = cnx.cursor()

        query = "SELECT * FROM Inventory"
        cursor.execute(query)

        for (ProductCode, ProductName, Quantity, Profit) in cursor:
            print("=============================================================")
            print(f"Product Code    : {ProductCode}")
            print(f"Product Name    : {ProductName}")
            print(f"Quantity        : {Quantity}")
            print(f"Profit          : {Profit}")
            print("=============================================================")

        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_inventory():
    try:
        clear_screen()
        cnx = get_connection()
        cursor = cnx.cursor()

        product_code = int(input("Enter Product Code to delete: "))

        cursor.execute("DELETE FROM Inventory WHERE ProductCode = %s", (product_code,))
        cnx.commit()

        print("Inventory record deleted successfully.")
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

