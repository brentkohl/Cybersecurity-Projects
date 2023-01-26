chars = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"]


def encode(message, offset=13):
    enc_chars = str.maketrans(
        f"{chars[0]}{chars[1]}",
        f"{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}",
    )
    return str.translate(message, enc_chars)


def decode(message, offset=13):
    dec_chars = str.maketrans(
        f"{chars[0][offset:]}{chars[0][:offset]}{chars[1][offset:]}{chars[1][:offset]}",
        f"{chars[0]}{chars[1]}",
    )
    return str.translate(message, dec_chars)


get_option = input("Choose [e]ncode or [d]ecode (Default: e): ")
if get_option == "e":
    message = input("Enter your plaintext message: ")
    offset = int(input("Choose the shift (1-26): "))
    if offset < 1 or offset > 26:
        raise Exception(f"Invalid entry: {offset}")
    else:
        print(f"Your encoded message: {encode(message, offset)}")
elif get_option == "d":
    message = input("Enter your ciphertext message: ")
    offset = int(input("Choose the shift (1-26): "))
    if offset < 1 or offset > 26:
        raise Exception(f"Invalid entry: {offset}")
    else:
        print(f"Your decoded message: {decode(message, offset)}")
else:
    raise Exception(f"Invalid option: {get_option}")
