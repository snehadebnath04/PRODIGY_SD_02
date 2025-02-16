import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Guessing Game!")
    print("I have picked a number between 1 and 100. Can you guess what it is?")
    
    while not guessed:
        # Take user's guess
        user_guess = int(input("Enter your guess: "))
        attempts = attempts + 1
        
        # Compare the guess with the generated number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
            print(f"It took you {attempts} attempts to guess the correct number.")
    
    # play again
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thank you for playing! Goodbye.")

guessing_game()
