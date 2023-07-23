from binascii import unhexlify
import json

path = "Crypt_message.json"

with open(path, "r") as file:
    data = json.loads(file.read())


def number_to_text(text):
    text_un = unhexlify(hex(text)[2:])
    return text_un.decode()


def RSA_Decrypt(encrypted_file):
    return pow(encrypted_file[0], encrypted_file[1], encrypted_file[2])


def main():
    print(number_to_text(RSA_Decrypt(data)))
    print("Success!")


if __name__ == "__main__":
    main()
