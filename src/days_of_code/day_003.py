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

        scenario1 = self.scenario(self.scenes["s1"])
        if scenario1 is False:
            return self.game_over()

        scenario2 = self.scenario(self.scenes["s2"])
        if scenario2 is False:
            return self.game_over()

        scenario3 = self.scenario(self.scenes["s3"], False)
        return self.game_over(scenario3)

    def print_game_intro(self):
        print(self.ascii_banner)
        print("Welcome to Treasure Island.")
        print("Your mission is to find the treasure.\n")

    def render_scene(self, description, question):
        print(description + " ")
        player_response = input(question + " ").strip()
        print(f"Your choice: {player_response}")
        return player_response

    def update_messages(self, message):
        # To avoid cluttering self.messages with None elements
        if message is not None:
            self.messages.append(message)

    def respond_to_player(self, choices, player_response):
        for my_dict in choices:
            if player_response.lower() == my_dict["choice"]:
                self.update_messages(my_dict["message"])
                return my_dict["bool"]

    def finish_scenario(self, pc_response, default_message, default_bool):
        if pc_response is None:
            self.update_messages(default_message)
            return default_bool
        else:
            return pc_response

    def scenario(self, hsh, default_bool=False):
        description, question, choices, default_message = (
            hsh["description"],
            hsh["question"],
            hsh["choices"],
            hsh["default_message"],
        )

        player_response = self.render_scene(description, question)
        pc_response = self.respond_to_player(choices, player_response)
        return self.finish_scenario(pc_response, default_message, default_bool)

    def final_message(self):
        joined_messages = "\n".join(self.messages)
        print(joined_messages)
        return joined_messages

    def finalize_messages(self, bool):
        if bool is False or None:
            self.messages.append("Game over.")
        else:
            self.messages.append("You win!")

    def game_over(self, bool=False):
        self.finalize_messages(bool)
        return self.final_message()


def main():
    new_game = Game()
    new_game.play()


if __name__ == "__main__":
    main()
