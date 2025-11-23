def grocery_checkout():
    # Predefined grocery database
    store_items = {
        "apple": 0.50,
        "banana": 0.30,
        "milk": 2.50,
        "bread": 2.00,
        "eggs": 3.00,
        "cheese": 4.50
    }
    
    cart = [] # List of dictionaries for the final bill
    
    print("Grocery Store Checkout")
    print("Available items:", ", ".join(store_items.keys()))
    
    while True:
        item_name = input("\nEnter item name to add (or 'checkout' to finish): ").strip().lower()
        
        if item_name == 'checkout':
            break
            
        if item_name in store_items:
            try:
                qty = int(input(f"How many {item_name}s? "))
                if qty > 0:
                    price = store_items[item_name]
                    subtotal = price * qty
                    # Add detailed object to cart
                    cart.append({
                        "item": item_name,
                        "price": price,
                        "qty": qty,
                        "subtotal": subtotal
                    })
                    print(f"Added {qty} {item_name}(s).")
                else:
                    print("Quantity must be greater than 0.")
            except ValueError:
                print("Invalid input. Please enter a number for quantity.")
        else:
            print("Item not found in store. Try again.")

    # Final Bill
    print("\n" + "*"*40)
    print("FINAL BILL")
    print("*"*40)
    grand_total = 0
    
    print(f"{'Item':<10} {'Qty':<5} {'Price':<8} {'Subtotal'}")
    for entry in cart:
        print(f"{entry['item']:<10} {entry['qty']:<5} ${entry['price']:<7.2f} ${entry['subtotal']:.2f}")
        grand_total += entry['subtotal']
        
    print("-" * 40)
    print(f"GRAND TOTAL: ${grand_total:.2f}")

# Run the program
grocery_checkout()