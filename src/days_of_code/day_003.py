"""Day 3: Treasure Island"""

import os
import json


class Game:

    def __init__(self):
        self.messages = []
        self.assets_path = os.path.join(os.getcwd(), "src", "days_of_code", "assets")
        json_path = os.path.join(self.assets_path, "day_003_scenarios.json")
        self.scenes = json.load(open(json_path, "r"))
        ascii_path = os.path.join(self.assets_path, "ascii_treasure.txt")
        self.ascii_banner = open(ascii_path, "r").read()

    def play(self):
        self.print_game_intro()

        if self.scenario(self.scenes["s1"]) is False:
            return self.game_over()

        if self.scenario(self.scenes["s2"]) is False:
            return self.game_over()

        return self.game_over(self.scenario(self.scenes["s3"], False))

    def print_game_intro(self):
        print(self.ascii_banner)
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.\n")

    def scenario(self, hsh, default=False):
        description, question, choices, default_message = (
            hsh["description"],
            hsh["question"],
            hsh["choices"],
            hsh["default_message"],
        )

        print(description + " ")
        response = input(question + " ").strip()
        print(f"Your choice: {response}")

        for my_dict in choices:
            if response.lower() == my_dict["choice"]:
                # To avoid cluttering self.messages with None elements
                if my_dict["message"] is not None:
                    self.messages.append(my_dict["message"])
                return my_dict["bool"]

        self.messages.append(default_message)
        return default

    def game_over(self, bool=False):
        if bool is False:
            self.messages.append("Game over.")
        else:
            self.messages.append("You win!")

        joined_messages = "\n".join(self.messages)
        print(joined_messages)
        return joined_messages


def main():
    new_game = Game()
    new_game.play()


if __name__ == "__main__":
    main()
