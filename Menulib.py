import Purchases
import Sales
import Inventory

def MenuPurchases():
    while True:
        print("\t\t\t Purchase Record Management\n")
        print("=================================================================")
        print("1. Add Purchase Record")
        print("2. Print all Purchases")
        print("3. Delete Purchase Record")
        print("4. Return to Main Menu")
        print("=================================================================")
        choice = int(input("Enter Choice between 1 to 4 -------> : "))
        if choice == 1:
            Purchases.insert_purchase()
        elif choice == 2:
            Purchases.read_all_purchases()
        elif choice == 3:
            Purchases.delete_purchase()
        elif choice == 4:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuSales():
    while True:
        print("\t\t\t Sales Record Management\n")
        print("=================================================================")
        print("1. Add Sales Record")
        print("2. Print all Sales")
        print("3. Delete Sales Record")
        print("4. Return to Main Menu")
        print("=================================================================")
        choice = int(input("Enter Choice between 1 to 5 ------> : "))
        if choice == 1:
            Sales.insert_sale()
        elif choice == 2:
            Sales.read_all_sales()
        elif choice == 3:
            Sales.delete_sale()
        elif choice == 4:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuInventory():
    while True:
        print("\t\t\t Inventory Record Management\n")
        print("=================================================================")
        print("1. Select all Products")
        print("2. Onboard a Product")
        print("3. Delete a Product")
        print("4. Return to Main Menu")
        print("=================================================================")
        choice = int(input("Enter Choice between 1 to 4 ------> : "))
        if choice == 1:
            Inventory.read_all_inventory()
        elif choice == 2:
            Inventory.insert_inventory()
        elif choice ==3:
            Inventory.delete_inventory()
        elif choice ==4:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")
