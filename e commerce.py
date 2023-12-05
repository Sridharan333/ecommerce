import uuid

# A product class to store details about each product
class Product:
    def __init__(self, name, price, quantity):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price
        self.quantity = quantity

# An order class to store details about each order
class Order:
    def __init__(self, customer_name, products):
        self.id = uuid.uuid4()
        self.customer_name = customer_name
        self.products = products

# List of available products
available_products = [
    Product("Product 1", 100, 5),
    Product("Product 2", 200, 3),
    Product("Product 3", 300, 2),
]

# List of placed orders
placed_orders = []

# Function to print product details
def print_product_details(product):
    print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

# Function to print order details
def print_order_details(order):
    print(f"Order ID: {order.id}, Customer Name: {order.customer_name}")
    print("Products:")
    for product in order.products:
        print_product_details(product)

# Function to list all available products
def list_available_products():
    for product in available_products:
        print_product_details(product)

# Function to add a new product
def add_product(name, price, quantity):
    new_product = Product(name, price, quantity)
    available_products.append(new_product)
    print_product_details(new_product)

# Function to place an order
def place_order(customer_name, product_ids):
    products = [product for product in available_products if product.id in product_ids]
    if not products:
        print("No valid products selected.")
        return

    order = Order(customer_name, products)
    placed_orders.append(order)
    print_order_details(order)

# Main function to run the e-commerce program
def main():
    while True:
        print("\n1. List available products")
        print("2. Add a new product")
        print("3. Place an order")
        print("4. List all placed orders")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_available_products()
        elif choice == "2":
            name = input("Enter product name: ")
            price = int(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(name, price, quantity)
        elif choice == "3":
            customer_name = input("Enter customer name: ")
            product_ids = [uuid.UUID(id) for id in input("Enter product IDs separated by spaces: ").split()]
            place_order(customer_name, product_ids)
        elif choice == "4":
            for order in placed_orders:
                print_order_details(order)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()