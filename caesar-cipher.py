def main():
    print("Welcome to CaesarCipher.")
    user_choice = int(input("""
    Please select an option (1/2)
    1. Encrypt
    2. Decrypt
    """))
    if user_choice == 1:
        plaintext = input("Please enter a message: ")
        shift = int(input("Please enter the shift: "))
        print(encrypt(plaintext, shift))
    elif user_choice == 2:
        pass
    else:
        print("Please enter a valid choice (1/2).")
        main()  # Re-run the main function


def encrypt(e_plaintext, e_shift):  # Encrypt Function
    e_output = ""  # Blank output
    for i in e_plaintext:
        e_ascii = ord(i)  # Convert to the ascii value
        if e_ascii < 64:
            e_output = e_output + i
        else:
            e_ascii = e_ascii + e_shift % 65  # Adds the shift, rotates back to A
            e_output = e_output + chr(e_ascii)
    return e_output


def decrypt():  # Decrypt Function
    pass


main()  # Run the program


