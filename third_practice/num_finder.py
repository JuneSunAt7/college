def finder():
    with open('example.txt', 'r') as file:
        content = file.read()

    # find all digits in the content
    digits = [int(c) for c in content if c.isdigit()]  # extract digits and convert to integers

    # calculate the sum
    total_sum = sum(digits)

    print(f"Сумма цифр в файле: {total_sum}.")

if __name__ == "__main__":
    finder()