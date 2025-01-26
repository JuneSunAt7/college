def main():
    # ask the user to input a number
    user_input = input("input numb: ")

    try:
        # convert the input to an integer
        number = int(user_input)

        # check if the num is even or odd
        if number % 2 == 0:
            print(f"num {number} is even.")
        else:
            print(f"num {number} is odd.")

        if number % 3 == 0:
            print("divisible by 3.")
        else:
            print("no divisible by 3.")

        if number % 5 == 0:
            print("divisible by 5.")
        else:
            print(" no divisible by 5.")

    except ValueError:
        # handle the case where the input is not a valid integer
        print("uncorrect num.")

if __name__ == "__main__":
    main()