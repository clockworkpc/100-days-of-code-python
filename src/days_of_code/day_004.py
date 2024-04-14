"""Day 4: Rock Paper Scissors"""

import os
import json
import random


class Game:

    def __init__(self):
        self.ascii_path = os.path.join(
            os.getcwd(), "src", "days_of_code", "assets", "ascii"
        )
        json_path = os.path.join(
            os.getcwd(), "src", "days_of_code", "assets", "json", "day_004_rules.json"
        )

        self.rules = json.load(open(json_path, "r"))

    def play_round(self, hand1, hand2):
        return self.rules[hand1]["results"][hand2]

    def find_key_by_code(self, target_code):
        for key, value in self.rules.items():
            if value["code"] == target_code:
                return key
        return None

    def instructions(self):
        options = []
        for k, v in self.rules.items():
            options.append(f"{str( v['code'] )} for { k.capitalize() }")

        options = ", ".join(options)
        return " ".join(["What do you choose? Type", options, ": "])

    def print_hands(self, user_hand, pc_hand):
        user_ascii_path = os.path.join(self.ascii_path, f"{user_hand}.txt")
        user_ascii = ascii_img = open(user_ascii_path, "r").read()
        pc_ascii_path = os.path.join(self.ascii_path, f"{pc_hand}.txt")
        pc_ascii = ascii_img = open(pc_ascii_path, "r").read()
        print("You chose:")
        print(user_ascii)
        print("Computer chose:")
        print(pc_ascii)

    def print_outcome(self, result):
        if result == "win":
            print("You win!")
        elif result == "draw":
            print("You lose!")
        else:
            print("It's a draw!")

    def play(self, preset_hand=None):
        os.system("clear")
        user_choice = input(self.instructions())
        user_hand = self.find_key_by_code(int(user_choice))

        if user_hand is None:
            print("This option does not exist.")
            return

        if preset_hand is None:
            random_hand = random.choice(list(self.rules.keys()))

        pc_hand = preset_hand or random_hand
        result = self.play_round(user_hand, pc_hand)

        self.print_hands(user_hand, pc_hand)
        self.print_outcome(result)

        return result


def main():
    new_game = Game()
    new_game.play()


if __name__ == "__main__":
    main()
