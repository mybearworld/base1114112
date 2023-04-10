"""Encode and decode base1114112."""


import sys


def decode(number):
    """
    It takes a base 1114112 number and returns a decimal number

    :param number: the base 1114112 number to be decoded
    :return: the decimal number
    """

    result = 0
    j = 1
    for i in number[::-1]:
        result += ord(i)*j
        j *= 1114112
    return result


# from https://stackoverflow.com/questions/2267362/
def encode(number):
    """
    It converts a number to a string of characters, where each character is a
    digit in base 1114112

    :param number: the number to encode
    :return: a string of characters
    """

    if number == 0:
        return [0]
    digits = []
    while number:
        digits.append(int(number % 1114112))
        number //= 1114112
    return "".join(list(map(chr, digits[::-1])))


def main():
    """Main function."""

    print("Note: When decoding, to stop, press new line and then CTRL+D "
          "(or, on Windows, CTRL+Z).\n")

    while True:
        if input("[E]ncode or [D]ecode? ").lower() == "e":
            encoded = encode(int(input()))

            # Surrogates
            surrogate = ""
            for i in encoded:
                if not ord(i) in range(0xd800, 0xdfff):
                    surrogate += i
            if encoded != surrogate:
                to_output = surrogate
                print(surrogate)
            else:
                to_output = encoded
                print(encoded)

            # Hex
            for i in encoded:
                hexa = hex(ord(i))[2:]
                print((6-len(hexa))*"0"+hexa, end=" ")

            # As ASCII
            print(f"\n{to_output !a}")
            if encoded != surrogate:
                print("WARNING: Output contains surrgoates. They have been "
                "removed for printability, but they are still included in the "
                "hex.")
            print()
        else:
            read = sys.stdin.read()[:-1]
            print(decode(read))
        print("\n")


if __name__ == "__main__":
    main()
