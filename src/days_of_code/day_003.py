"""Day 3: Treasure Island"""

import os

assets_path = os.path.join(os.getcwd(), "src", "days_of_code", "assets")


class Game:

    def __init__(self):
        self.messages = []

    def print_banner_ascii(self):
        file_path = os.path.join(assets_path, "ascii_treasure.txt")
        with open(file_path, "r") as file:
            file_contents = file.read()
            print(file_contents)

        print("Welcome to Treasure Island.")
        print("Your mission to find the treasure.")

    def scenario(self, intro, choose, choices, default=True):
        print(intro + " ")
        choice = input(choose + " ").strip()
        print(f"CHOICE: {choice}")
        for my_dict in choices:
            if choice.lower() == my_dict["choice"]:
                if my_dict["message"] is not None:
                    self.messages.append(my_dict["message"])
                return my_dict["bool"]
        return default

    def scenario1(self):
        intro = "You reach a fork in the road."
        choose = "left or right?"
        choices = [{"choice": "right", "message": "Fall into a hole.", "bool": False}]
        return self.scenario(intro, choose, choices)

    def scenario2(self):
        intro = "You reach a river and see a ferry in the distance."
        choose = "swim or wait?"
        choices = [{"choice": "swim", "message": "Attacked by trout.", "bool": False}]
        return self.scenario(intro, choose, choices)

    def scenario3(self):
        intro = "You arrive at three doors."
        choose = "Which door?  Red, Blue, Yellow? "
        choices = [
            {"choice": "yellow", "message": None, "bool": True},
            {"choice": "red", "message": "Burned by fire.", "bool": False},
            {"choice": "blue", "message": "Eaten by beasts.", "bool": False},
        ]
        return self.scenario(intro, choose, choices, False)

    def game_over(self, bool=False):
        if bool is False:
            self.messages.append("Game over.")
        else:
            self.messages.append("You win!")

        joined_messages = "\n".join(self.messages)
        print(joined_messages)
        return joined_messages

    def play(self):
        self.print_banner_ascii()

        if self.scenario1() is False:
            return self.game_over()

        if self.scenario2() is False:
            return self.game_over()

        return self.game_over(self.scenario3())


def main():
    new_game = Game()
    new_game.play()


if __name__ == "__main__":
    main()
