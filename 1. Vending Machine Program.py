
# 1. Vending machine

# Build a program that:
# Displays a list of snacks and drinks with item numbers and prices.
# Asks the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types “done”.
# Finally prints a receipt showing:
# List of selected items with prices
# Total cost
# Skills practiced: loops, input(), conditionals, lists/dictionaries, sum(), print formatting


def vending_machine():
    # Inventory: ID mapping to Dictionary of details
    inventory = {
        "1": {"name": "Soda", "price": 1.50},
        "2": {"name": "Chips", "price": 1.00},
        "3": {"name": "Candy Bar", "price": 1.25},
        "4": {"name": "Water", "price": 0.75},
        "5": {"name": "Juice", "price": 2.00}
    }
    
    cart = [] # List to store selected items
    
    print("Welcome to the Vending Machine")
    
    while True:
        # Display Menu
        print("\nAvailable Items:")
        for key, item in inventory.items():
            print(f"{key}. {item['name']} - ${item['price']:.2f}")
            
        choice = input("\nEnter item number (or type 'done' to finish): ").strip().lower()
        
        if choice == 'done':
            break
        
        if choice in inventory:
            selected_item = inventory[choice]
            cart.append(selected_item)
            print(f"Added {selected_item['name']} to cart.")
        else:
            print("Invalid selection. Please try again.")

    # Receipt Generation
    print("\n" + "="*30)
    print("       RECEIPT       ")
    print("="*30)
    
    total = 0
    for item in cart:
        print(f"{item['name']:<20} ${item['price']:.2f}")
        total += item['price']
        
    print("-" * 30)
    print(f"TOTAL COST:{' ':>9} ${total:.2f}")
    print("="*30)

# Run the program
vending_machine()