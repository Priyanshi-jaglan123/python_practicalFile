def caesar_cipher(text, shift, mode):
    result = ""

    if mode.lower() == "decrypt":
        shift = -shift

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result


# Main Program
print("===== Caesar Cipher Tool =====")

text = input("Enter the message: ")

while True:
    try:
        shift = int(input("Enter shift key: "))
        break
    except ValueError:
        print("Please enter a valid integer.")

mode = input("Enter mode (encrypt/decrypt): ")

if mode.lower() not in ["encrypt", "decrypt"]:
    print("Invalid mode! Choose 'encrypt' or 'decrypt'.")
else:
    output = caesar_cipher(text, shift, mode)
    print("\nResult:", output)