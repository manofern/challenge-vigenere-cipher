alphabet_number = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
}

alphabet_word = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'I',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z',
}


def menu():
    print(
        "|-----------------|\n"
        "| Vigenère Cipher |\n"
        "|-----------------|\n"
        "|  1 - Encryption |\n"
        "|  2 - Decrypted  |\n"
        "|  0 - Exit       |\n"
        "|-----------------|")
    opt = int(input("| Type: "))
    print(
        '|-----------------|\n')
    return opt


def same_size(p, k):
    not_same_size = len(p) != len(k)
    size_even = len(p) % len(k) == 0

    if not_same_size:
        difference = len(p) - len(k)
        division = difference // len(k)
        k = k * (1 + division)
        if not size_even:
            remainder = difference % len(k)
            k = k + k[0:remainder]
    return k


def encryption(p, k):
    encrypted_phrase = ''
    k = same_size(p, k)

    for i, word in enumerate(p):
        encrypted_word = alphabet_number[p[i]] + alphabet_number[k[i]]
        while encrypted_word > 25:
            encrypted_word -= 26
        encrypted_phrase += alphabet_word[encrypted_word]

    return encrypted_phrase


def decryption(c, k):
    decrypted_phrase = ''
    k = same_size(c, k)

    for i, word in enumerate(c):
        encrypt_word = alphabet_number[c[i]] - alphabet_number[k[i]] + 26
        while encrypt_word > 25:
            encrypt_word -= 26
        decrypted_phrase += alphabet_word[encrypt_word]
    return decrypted_phrase


if __name__ == '__main__':
    while True:
        option = menu()
        if option == 1:
            print("|----------------------------------------------------|")
            phrase = input("| Type the phrase to encrypt: ").upper()
            key = input("| Type the key to encrypt: ").upper()
            encrypt = encryption(phrase, key)
            print(f"|----------------------------------------------------|\n"
                  f"| Encrypt: {encrypt} |\n"
                  f"|----------------------------------------------------|\n")

        elif option == 2:
            print("|----------------------------------------------------|")
            crypt_phrase = input("| Type the phrase to decrypted: ").upper()
            key = input("| Type the key to decrypted: ").upper()
            print("|----------------------------------------------------|")
            decrypt = decryption(crypt_phrase, key)
            print(f"|----------------------------------------------------|\n"
                  f"| Decrypt: {decrypt} |\n"
                  f"|----------------------------------------------------|\n")

        elif option == 0:
            break
