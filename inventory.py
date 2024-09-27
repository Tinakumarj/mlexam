class InventoryManager:
    def __init__(self):
        # Initialize an empty dictionary to store inventory items
        self.inventory = {}

    def add_item(self):
        """Adds a new item to the inventory based on user input."""
        item_id = input("Enter Item ID: ")
        if item_id in self.inventory:
            print(f"Error: Item ID {item_id} already exists in the inventory.")
            return
        item_name = input("Enter Item Name: ")
        category = input("Enter Category: ")
        stock_quantity = int(input("Enter Stock Quantity: "))
        price = float(input("Enter Price: "))
        
        self.inventory[item_id] = {
            'Item_Name': item_name,
            'Category': category,
            'Stock_Quantity': stock_quantity,
            'Price': price
        }
        print(f"Item '{item_name}' has been added to the inventory.")

    def remove_item(self):
        """Removes an item from the inventory based on user input."""
        item_id = input("Enter the Item ID to remove: ")
        if item_id in self.inventory:
            removed_item = self.inventory.pop(item_id)
            print(f"Item '{removed_item['Item_Name']}' has been removed from the inventory.")
        else:
            print(f"Error: Item ID {item_id} not found in the inventory.")

    def update_stock(self):
        """Updates the stock quantity of an item based on user input."""
        item_id = input("Enter the Item ID to update: ")
        if item_id in self.inventory:
            new_stock_quantity = int(input("Enter the new Stock Quantity: "))
            self.inventory[item_id]['Stock_Quantity'] = new_stock_quantity
            print(f"Stock quantity for item ID {item_id} has been updated to {new_stock_quantity}.")
        else:
            print(f"Error: Item ID {item_id} not found in the inventory.")

    def generate_low_stock_report(self):
        """Generates a report of items with stock quantities below a given threshold."""
        threshold = int(input("Enter the stock threshold to check for low stock: "))
        print(f"Low Stock Report (Threshold: {threshold}):")
        low_stock_items = {item_id: details for item_id, details in self.inventory.items()
                           if details['Stock_Quantity'] < threshold}
        if low_stock_items:
            for item_id, details in low_stock_items.items():
                print(f"Item ID: {item_id}, Name: {details['Item_Name']}, "
                      f"Category: {details['Category']}, Stock Quantity: {details['Stock_Quantity']}, "
                      f"Price: {details['Price']}")
        else:
            print("All items have sufficient stock.")

    def menu(self):
        """Menu to interact with the InventoryManager."""
        while True:
            print("\nInventory Management System")
            print("1. Add Item")
            print("2. Remove Item")
            print("3. Update Stock")
            print("4. Generate Low Stock Report")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.remove_item()
            elif choice == '3':
                self.update_stock()
            elif choice == '4':
                self.generate_low_stock_report()
            elif choice == '5':
                print("Exiting the Inventory Management System.")
                break
            else:
                print("Invalid choice, please try again.")

# Example of running the system
if __name__ == "__main__":
    manager = InventoryManager()
    manager.menu()
