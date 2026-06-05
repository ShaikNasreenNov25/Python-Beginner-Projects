from random import randint

def guessNumber(a,b):
    print("Welcome to the Number Guessing Game!🙌")
    print(f"Guess a number between {a} and {b}.\n")

    number = randint(a,b)
    count = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!\n")
            continue

        count += 1
        if number == user_guess:
            print("🎉 Congratulations! You guessed the number!.\n")
            break

        elif number > user_guess:
            print("Too low! Try again.\n")

        else:
            print("Too high! Try again.\n")

    print(f"You took {count} attempts.")

    def play_again():
        while True:
            again = input("Do you want to play again? (Yes/No): ").strip().lower()
            print()
            
            if again == "yes":
                guessNumber(a,b)
                break

            elif again == "no":
                print("Thanks for playing! Goodbye 👋")
                break

            else:
                print("Pleas Enter valid Yes on No only!")
    play_again()

guessNumber(1,100)

