def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # is char letter?
            start = ord('A') if char.isupper() else ord('a')
            # Shift char
            encrypted_char = chr(start + (ord(char) - start + shift) % 26)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


def tui(): # terminal user interface
    shift = int(input("shift val: "))

    with open('example.txt', 'r') as file:
        content = file.read()

    encrypted_content = caesar_cipher(content, shift)

    with open('encrypted_example.txt', 'w') as file:
        file.write(encrypted_content)
    print("encrypted.")

if __name__ == "__main__":
    tui()