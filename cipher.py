# add your code here
def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_text += encrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

# Ask the user for a plain text sentence
plain_text = input("Please enter a sentence: ")

# Encrypt the text using a right shift of 5
shift = 5
encrypted_text = caesar_cipher(plain_text, shift)

# Print the encrypted text
print("The encrypted sentence is:", encrypted_text)
