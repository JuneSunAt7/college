def changer():
    old_substring = input("Искомую подстроку: ")
    new_substring = input("Новую подстроку: ")

    with open('example.txt', 'r') as file:
        content = file.read()

    # replace
    modified_content = content.replace(old_substring, new_substring)

    # save
    with open('example.txt', 'w') as file:
        file.write(modified_content)

    print("replaced.")  # notify the user

if __name__ == "__main__":
    changer()