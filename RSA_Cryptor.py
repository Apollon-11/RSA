from binascii import hexlify
import json
import random


def text_to_number(text):
    text_encode = text.encode()
    return int(hexlify(text_encode), 16)


def RSA_Crypt(Message_input, prime1, prime2):
    Prime_multiplication = prime1 * prime2

    phi = (prime1-1)*(prime2-1)

    e = 7 * prime1

    d_number = pow(e, -1, phi)
    c = pow(Message_input, e, Prime_multiplication)
    return [c, d_number, Prime_multiplication]


def main():
    with open("Data_Prime_Number.json", "r") as f:
        prime_number = random.sample(json.loads(f.read()), 2)
    p = text_to_number(input())
    with open("Crypt_message.json", "w") as file:
        json.dump(RSA_Crypt(p, prime_number[0], prime_number[1]), file, indent=4)


if __name__ == "__main__":
    main()
