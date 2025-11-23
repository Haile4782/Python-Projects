def quiz_game():
    # List of dictionaries for questions
    questions = [
        {"q": "What is the capital of France?", "a": "paris"},
        {"q": "What is 5 + 7?", "a": "12"},
        {"q": "What color is the sky on a clear day?", "a": "blue"},
        {"q": "Who wrote 'Romeo and Juliet'?", "a": "shakespeare"},
        {"q": "Is Python a programming language? (yes/no)", "a": "yes"}
    ]
    
    score = 0
    wrong_answers = []
    
    print("General Knowledge Quiz")
    
    for item in questions:
        print(f"\nQuestion: {item['q']}")
        user_answer = input("Your Answer: ").strip().lower()
        
        # Check answer (checking if the user answer contains the key word)
        if user_answer == item['a']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            wrong_answers.append(item)
            
    # Final Results
    print("\n" + "="*30)
    print(f"Your Score: {score}/{len(questions)}")
    print("="*30)
    
    if wrong_answers:
        print("\nCorrections for wrong answers:")
        for item in wrong_answers:
            print(f"Q: {item['q']}")
            print(f"A: The correct answer was '{item['a'].capitalize()}'")
    else:
        print("Perfect score! Great job!")

# Run the program
quiz_game()