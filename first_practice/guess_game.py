import random

def guess_number_game():
    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 0
        print("I've guessed a number from 1 to 100.")

        while True:
            try:
                user_guess = int(input("Enter u num: "))
                attempts += 1

                if user_guess < number_to_guess:
                    print("number greater than.")
                elif user_guess > number_to_guess:
                    print("number less than.")
                else:
                    print(f"You guessed the number {number_to_guess} for {attempts} attempts.")
                    break
            except ValueError:
                print("Number is not correct.")

        play_again = input("would u like to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break
guess_number_game()