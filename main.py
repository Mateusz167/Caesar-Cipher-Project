from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(text, shift, direction):
    new_text = ""
    if direction == 'decode':
        shift *= -1
    for letter in text:
            if letter in alphabet:
                new_text += alphabet[alphabet.index(letter) + shift]
            else:
                new_text += letter
    print(f'The {direction}d text is: {new_text}')
program_stop = False

while not program_stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input(
        "Type the shift number:\n")) % 26  # Ensure the shift is within the range of 0-25
    caesar(text, shift, direction)
    want_continue = input("Do you want to continue? Type 'y' for yes or 'n' for no")
    if want_continue == 'n':
        program_stop = True
        print("Goodbye")