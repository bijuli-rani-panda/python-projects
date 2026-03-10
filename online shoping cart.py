# Online Shopping Cart System

# List to store cart items
cart = []

# Function to add item
def add_item():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    item = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(item)
    print("✅ Item added to cart!\n")


# Function to view cart
def view_cart():
    if not cart:
        print("🛒 Your cart is empty.\n")
        return

    print("\n🛍 Your Cart Items:")
    total = 0
    for i, item in enumerate(cart, start=1):
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"{i}. {item['name']} - ₹{item['price']} x {item['quantity']} = ₹{item_total}")

    print(f"\n💰 Total Bill: ₹{total}\n")


# Function to remove item
def remove_item():
    name = input("Enter product name to remove: ")

    for item in cart:
        if item["name"].lower() == name.lower():
            cart.remove(item)
            print("❌ Item removed from cart.\n")
            return

    print("Item not found in cart.\n")


# Main Menu
def main():
    while True:
        print("===== ONLINE SHOPPING CART =====")
        print("1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            print("🛒 Thank you for shopping!")
            break
        else:
            print("Invalid choice. Try again.\n")


# Run Program
if __name__ == "__main__":
    main()