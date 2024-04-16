"""Day 5: Password Generator"""

import random
import string


class Generator:
    def __init__(self):
        self.characters = {
            "letters": [c for c in string.ascii_letters],
            "numbers": [c for c in string.digits],
            "symbols": list("!#$%&()*+"),
        }

    def get_inputs(self):
        my_inputs = {}

        for char_type in self.characters.keys():
            msg = "How many %s would you like in your password? " % (char_type)
            my_inputs[char_type] = int(input(msg))

        return my_inputs

    def generate_password_list(self, my_inputs):
        password_list = []

        for key, my_int in my_inputs.items():
            for _ in range(my_int):
                char = random.choice(self.characters[key])
                password_list.append(char)

        return password_list

    def main(self):
        print("Welcome to the PyPassword Generator!")
        my_inputs = self.get_inputs()
        password_list = self.generate_password_list(my_inputs)
        shuffled_password_list = password_list.copy()
        random.shuffle(shuffled_password_list)
        password = "".join(shuffled_password_list)
        print(f"Your password: {password}")
        return password


def main():
    g = Generator()
    g.main()


if __name__ == "__main__":
    main()
