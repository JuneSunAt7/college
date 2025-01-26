
def main():
    # ask the user to choose a task
    print("choose a task:")
    print("1. sum of all numbers from 1 to n")
    print("2. even numbers from 1 to n")
    print("3. check if n is prime")
    print("4. largest digit in n")
    print("5. reverse a string")
    print("6. count words in a string")
    print("7. find all divisors of n")
    print("8. check if a string is a palindrome")
    print("9. find factorial of n")
    print("10. replace vowels in a string with '*'")


    task = int(input("please enter the task number (1-10): "))

    if task == 1:
        n = int(input("enter a number: "))
        total_sum = sum(range(1, n + 1))  # calculate sum from 1 to n
        print(f"sum of numbers from 1 to {n} is {total_sum}.")

    elif task == 2:
        n = int(input("enter a number: "))
        evens = [i for i in range(1, n + 1) if i % 2 == 0]  # find even numbers
        print(f"even numbers from 1 to {n}: {evens}.")

    elif task == 3:
        n = int(input("enter a number: "))
        is_prime = all(n % i != 0 for i in range(2, int(n ** 0.5) + 1)) if n > 1 else False  # check for prime
        print(f"{n} is {'prime' if is_prime else 'not prime'}.")

    elif task == 4:
        n = input("enter a number: ")
        largest_digit = max(n)  # find largest digit
        print(f"largest digit in {n} is {largest_digit}.")

    elif task == 5:
        s = input("enter a string: ")
        reversed_string = s[::-1]  # reverse the string
        print(f"reversed string: {reversed_string}.")

    elif task == 6:
        s = input("enter a string: ")
        word_count = len(s.split())  # count words
        print(f"number of words in the string: {word_count}.")

    elif task == 7:
        n = int(input("enter a number: "))
        divisors = [i for i in range(1, n + 1) if n % i == 0]  # find divisors
        print(f"divisors of {n}: {divisors}.")

    elif task == 8:
        s = input("enter a string: ")
        is_palindrome = s == s[::-1]  # check for palindrome
        print(f"{s} is {'a palindrome' if is_palindrome else 'not a palindrome'}.")

    elif task == 9:
        n = int(input("enter a number: "))
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i  # calculate factorial
        print(f"factorial of {n} is {factorial}.")

    elif task == 10:
        s = input("enter a string: ")
        replaced_string = ''.join('*' if c in 'aeiouAEIOU' else c for c in s)  # replace vowels
        print(f"string with vowels replaced: {replaced_string}.")
if __name__ == "__main__":
    main()