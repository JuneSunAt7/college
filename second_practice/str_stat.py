def main():
    # ask the user to input a str
    user_input = input("please enter a str: ")

    # init counters for different char types
    total_chars = len(user_input)  # total number of chars
    letters = sum(c.isalpha() for c in user_input)  # count letters
    digits = sum(c.isdigit() for c in user_input)  # count digits
    special_chars = sum(not c.isalnum() and not c.isspace() for c in user_input)  # count special chars

    # res
    print(f"total characters: {total_chars}")
    print(f"letters: {letters}")
    print(f"digits: {digits}")
    print(f"special characters: {special_chars}")

if __name__ == "__main__":
    main()