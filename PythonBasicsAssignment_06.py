# Ramzi Jarad
# Python Basics Assignment 06
# Store System

# function to add a new product
def add_new_product():
    num_products = int(input("Enter the number of products: "))
    if num_products <= 0:
        print("Number of products should be greater than 0")
        return
    for i in range(num_products):
        name = input(f"Enter Product {i+1} Name: ")
        qty = int(input(f"Enter Product {i+1} Quantity: "))
        price = float(input(f"Enter Product {i+1} Price: "))
        products.append({"name": name, "qty": qty, "price": price})
    print("Product(s) have been added successfully")

# function to search for a product by name
def search_product_by_name():
    search_term = input("Enter product name or substring: ")
    found_products = []
    for product in products:
        if search_term.lower() in product["name"].lower():
            found_products.append(product)
    if found_products:
        for product in found_products:
            print(f"Product Name: {product['name']}, Product Quantity: {product['qty']}, Product Price: {product['price']}")
    else:
        print("No products found")


products = []
while True:
    choice = int(input("Select 1. For Add New Product\n"
                       "Select 2. Search using Product Name\n"
                       "Select 3. Exit\n"
                       "==>:"))
    if choice == 1:
        add_new_product()
    elif choice == 2:
        search_product_by_name()
    elif choice == 3:
        print("bye bye :)")
        break
    else:
        print("Invalid choice")