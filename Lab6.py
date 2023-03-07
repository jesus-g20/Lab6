def encode(password):
    encoded = ""
    for i in password:
        digit = int(i) + 3
        encoded += str(digit)
    return encoded
# returns encoded password with larger digits


def decode(password):
    decoded = ""
    for i in password:
        digit = int(i) - 3
        decoded += str(digit)
    return decoded
# returns decoded password with lower digits

def main():

    encoded = None

    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")

        menu_selection = int(input("Please enter an option: "))
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)

        elif menu_selection == 2:
            decoded = decode(encoded)
            print("The encoded password is " + encoded + " and the original password is " + decoded + ".")

        elif menu_selection == 3:
            break

if __name__ == "__main__":
    main()