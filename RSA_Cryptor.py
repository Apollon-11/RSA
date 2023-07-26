from binascii import hexlify
import json

with open("Key_Gen.json", "r") as file:
    data = json.loads(file.read())


def text_to_number(text):
    text_encode = text.encode()
    return int(hexlify(text_encode), 16)


def RSA_Crypt(Message_input, Open_Key, Prime_Multiplication):
    Crypt_Message = pow(Message_input, Open_Key, Prime_Multiplication)
    return Crypt_Message


def main():
    Message_in = text_to_number(input())
    Crypt_Message = RSA_Crypt(Message_in, data[0], data[1])
    with open("Crypt_message.json", "w") as file:
        json.dump(Crypt_Message, file, indent=4)


if __name__ == "__main__":
    main()
