def movie_booking():
    # Nested dictionary: Movie Title -> Details
    movies = {
        "1": {"title": "Inception", "time": "7:00 PM", "price": 12.00},
        "2": {"title": "The Lion King", "time": "5:30 PM", "price": 10.00},
        "3": {"title": "Avengers", "time": "8:15 PM", "price": 14.00}
    }
    
    total_bookings = 0
    total_cost = 0
    
    print("Movie Theater Booking System")
    
    while True:
        print("\nNow Showing:")
        for key, m in movies.items():
            print(f"{key}. {m['title']} @ {m['time']} (${m['price']})")
            
        choice = input("\nSelect a movie number: ").strip()
        
        if choice in movies:
            movie = movies[choice]
            try:
                tickets = int(input(f"How many tickets for {movie['title']}? "))
                if tickets > 0:
                    cost = tickets * movie['price']
                    print(f"Cost for {tickets} tickets: ${cost:.2f}")
                    
                    confirm = input("Confirm booking? (yes/no): ").lower()
                    if confirm == 'yes':
                        total_bookings += tickets
                        total_cost += cost
                        print("Booking confirmed!")
                    else:
                        print("Booking cancelled.")
                else:
                    print("Must buy at least 1 ticket.")
            except ValueError:
                print("Invalid number entered.")
        else:
            print("Invalid movie selection.")
            
        again = input("\nBook another movie? (yes/no): ").lower()
        if again != 'yes':
            break
            
    print("\n--- Final Summary ---")
    print(f"Total Tickets Booked: {total_bookings}")
    print(f"Total Cost: ${total_cost:.2f}")

# Run the program
movie_booking()