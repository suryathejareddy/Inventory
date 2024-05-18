import mysql.connector
from mysql.connector import errorcode
import os

def clear_screen():
    # Print multiple newlines to simulate clearing the screen
    print("\n" * 100)

def get_connection():
    return mysql.connector.connect(user='root', password='hello123', host='localhost', database='Inventory')

def insert_sale():
    try:
        clear_screen()
        cnx = get_connection()
        cursor = cnx.cursor()

        product_code = int(input("Enter Product Code: "))
        sale_quantity = int(input("Enter Sale Quantity: "))
        sales_date = input("Enter Sales Date (YYYY-MM-DD): ")
        sales_price = int(input("Enter Sales Price: "))

        query = '''
        INSERT INTO Sales (ProductCode, Sale_Quantity, SalesDate, SalesPrice)
        VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(query, (product_code, sale_quantity, sales_date, sales_price))
        cnx.commit()

        update_inventory_sale(product_code, sale_quantity, sales_price)

        print("Sale record inserted successfully.")
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def update_inventory_sale(product_code, sale_quantity, sales_price):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()

        # Get current quantity and profit from Inventory
        cursor.execute("SELECT Quantity, Profit FROM Inventory WHERE ProductCode = %s", (product_code,))
        inventory_result = cursor.fetchone()

        if inventory_result:
            current_quantity = inventory_result[0]
            current_profit = inventory_result[1]

            if current_quantity >= sale_quantity:
                # Calculate revenue from sales
                sales_revenue = sale_quantity * sales_price

                # Get purchase cost from Purchases
                cursor.execute("SELECT PurchasePrice FROM Purchases WHERE ProductCode = %s", (product_code,))
                purchase_result = cursor.fetchone()

                if purchase_result:
                    purchase_price = purchase_result[0]
                    total_purchase_cost = sale_quantity * purchase_price
                    profit_from_sale = sales_revenue - total_purchase_cost
                    new_quantity = current_quantity - sale_quantity
                    new_profit = current_profit + profit_from_sale

                    cursor.execute("UPDATE Inventory SET Quantity = %s, Profit = %s WHERE ProductCode = %s", (new_quantity, new_profit, product_code))
                    cnx.commit()
                else:
                    print("Error: No purchase record found for this product.")
            else:
                print("Error: Not enough quantity in inventory to complete the sale.")
        else:
            print("Error: Product does not exist in inventory.")

        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def read_all_sales():
    try:
        clear_screen()
        cnx = get_connection()
        cursor = cnx.cursor()

        query = "SELECT * FROM Sales"
        cursor.execute(query)

        for (ProductCode, Sale_Quantity, SalesDate, SalesPrice) in cursor:
            print("=============================================================")
            print(f"Product Code    : {ProductCode}")
            print(f"Sale Quantity   : {Sale_Quantity}")
            print(f"Sales Date      : {SalesDate}")
            print(f"Sales Price     : {SalesPrice}")
            print("=============================================================")

        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_sale():
    try:
        clear_screen()
        cnx = get_connection()
        cursor = cnx.cursor()

        product_code = int(input("Enter Product Code to delete: "))

        cursor.execute("DELETE FROM Sales WHERE ProductCode = %s", (product_code,))
        cnx.commit()

        print("Sale record deleted successfully.")
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

