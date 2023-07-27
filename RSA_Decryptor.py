from binascii import unhexlify
import json
import random
from time import sleep


def number_to_text(text):
    text_un = unhexlify(hex(text)[2:])
    return text_un.decode()


def Key_Gen(prime1, prime2):
    Prime_multiplication = prime1 * prime2

    phi = (prime1 - 1) * (prime2 - 1)

    Open_Key = 7 * prime1

    try:
        Secret_Key = pow(Open_Key, -1, phi)
    except ValueError:
        return print("Failed to generate keys, please try again")
    return [Secret_Key, Open_Key, Prime_multiplication]


def Decrypt(Crypt_message, Secret_Key, Prime_Multiplication):
    return pow(Crypt_message, Secret_Key, Prime_Multiplication)


def expectation(num):
    sleep(num)


def main():
    with open("Data_Prime_Number.json", "r") as f:
        prime_number = random.sample(json.loads(f.read()), 2)
    with open("Key_Gen.json", "w") as file:
        try:
            json.dump(Key_Gen(prime_number[0], prime_number[1])[1:], file, indent=4)
        except TypeError:
            return
    print("Please wait 25 seconds")
    expectation(25)
    with open("Crypt_message.json", "r") as r:
        Crypt_Message = json.loads(r.read())
    l = Decrypt(Crypt_Message, Key_Gen(prime_number[0], prime_number[1])[0], Key_Gen(prime_number[0], prime_number[1])[2])
    print(number_to_text(l))


if __name__ == "__main__":
    main()
