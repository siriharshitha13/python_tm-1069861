class ProductManager:
    def __init__(self):
        self.products = {}
        self.product_id_counter = 1

    # Add a new product
    def add_product(self):
        name = input("Enter product name: ")
        category = input("Enter product category: ")
        price = float(input("Enter product price: "))
        product_id = self.product_id_counter
        self.products[product_id] = {
            'name': name,
            'category': category,
            'price': price
        }
        self.product_id_counter += 1
        print(f"Product added with ID: {product_id}")
    
    # Update an existing product
    def update_product(self):
        pid = int(input("Enter product ID to update: "))
        if pid in self.products:
            name = input("Enter new product name (or leave blank): ")
            category = input("Enter new product category (or leave blank): ")
            price = input("Enter new product price (or leave blank): ")
            
            if name:
                self.products[pid]['name'] = name
            if category:
                self.products[pid]['category'] = category
            if price:
                self.products[pid]['price'] = float(price)
                
            print(f"Product {pid} updated successfully.")
        else:
            print(f"Product with ID {pid} not found.")

    # Delete a product by PId
    def delete_product(self):
        pid = int(input("Enter product ID to delete: "))
        if pid in self.products:
            del self.products[pid]
            print(f"Product {pid} deleted.")
        else:
            print(f"Product with ID {pid} not found.")
    
    # Get product by PId
    def get_product_by_id(self):
        pid = int(input("Enter product ID: "))
        product = self.products.get(pid, None)
        if product:
            print(f"Product ID {pid}: {product}")
        else:
            print(f"Product with ID {pid} not found.")

    # Get all products
    def get_all_products(self):
        if not self.products:
            print("No products available.")
        else:
            for pid, product in self.products.items():
                print(f"Product ID {pid}: {product}")

    # Get products by category
    def get_products_by_category(self):
        category = input("Enter category: ")
        result = {pid: prod for pid, prod in self.products.items() if prod['category'] == category}
        if result:
            for pid, product in result.items():
                print(f"Product ID {pid}: {product}")
        else:
            print(f"No products found in category '{category}'.")

    # Get products between two prices
    def get_products_between_prices(self):
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        result = {pid: prod for pid, prod in self.products.items() if min_price <= prod['price'] <= max_price}
        if result:
            for pid, product in result.items():
                print(f"Product ID {pid}: {product}")
        else:
            print(f"No products found in the price range {min_price} to {max_price}.")

    # Exit the program
    def exit_program(self):
        print("Exiting the program.")
        exit()

# Menu-driven interface
def show_menu():
    print("\nProduct Manager Menu:")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Get Product By PId")
    print("5. Get All Products")
    print("6. Get Products By Category")
    print("7. Get Products Between Prices")
    print("8. Exit")

def main():
    manager = ProductManager()
    
    # Dictionary to simulate switch-case behavior
    menu_options = {
        1: manager.add_product,
        2: manager.update_product,
        3: manager.delete_product,
        4: manager.get_product_by_id,
        5: manager.get_all_products,
        6: manager.get_products_by_category,
        7: manager.get_products_between_prices,
        8: manager.exit_program
    }

    while True:
        show_menu()
        try:
            option = int(input("Choose an option: "))
            if option in menu_options:
                menu_options[option]()  # Call the selected function
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

