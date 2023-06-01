import re
from unidecode import unidecode


def palindrome(word_sanitize, word):
    if word_sanitize[0:] == word_sanitize[::-1]:
        print(f"{word} é um Palíndromo")
    else:
        print(f"A palavra : {word} não é um Palíndromo")


def main():
    word = input().lower().strip()
    word_normalize = unidecode(word)
    print(word_normalize)
    word_sanitize = re.sub(r"[-,!?]*\s*\d*", "", word_normalize)
    print(word_sanitize)
    palindrome(word_sanitize, word)


if __name__ == "__main__":
    main()
