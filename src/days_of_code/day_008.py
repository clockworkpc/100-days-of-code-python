"""Day 8: Caesar Encryptor"""

import string


class Caesar:
    def __init__(self):
        self.alphabet = string.ascii_lowercase

    def shift_position(self, char, shift_amount):
        position = self.alphabet.index(char)
        new_index = (position + shift_amount) % 26
        return new_index

    def encode(self, start_text, shift_amount):
        end_text = ""
        for char in start_text:
            if char in self.alphabet:
                new_position = self.shift_position(char, shift_amount)
                end_text += self.alphabet[new_position]
            else:
                end_text += char

        return end_text

    def decode(self, start_text, shift_amount):
        return self.encode(start_text, shift_amount * -1)


def main():
    g = Caesar()
    g.run()


if __name__ == "__main__":
    main()
