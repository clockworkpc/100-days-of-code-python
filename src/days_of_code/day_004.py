"""Day 4: Rock Paper Scissors"""

import os
import sys
import json
import random


class Game:

    def __init__(self, rounds=5):
        assets_ary = "src/days_of_code/assets".split("/")
        self.ascii_path = os.path.join(os.getcwd(), *assets_ary, "ascii")
        json_ary = assets_ary + "json/day_004_rules.json".split("/")
        json_path = os.path.join(os.getcwd(), *json_ary)
        self.rules = json.load(open(json_path, "r"))
        self.score = {"user": 0, "pc": 0}
        self.rounds = rounds

    def play_round(self, hand1, hand2):
        return self.rules[hand1]["results"][hand2]

    def find_key_by_code(self, target_code):
        for key, value in self.rules.items():
            if value["code"] == target_code:
                return key
        return None

    def instructions(self):
        options_ary = [
            f"{v['code']} for {k.capitalize()}" for k, v in self.rules.items()
        ] + ["Q for Quit"]
        return " ".join(["Type", ", ".join(options_ary), "\nYour choice: "])

    def print_hands(self, user_hand, pc_hand):
        user_ascii_path = os.path.join(self.ascii_path, f"{user_hand}.txt")
        user_ascii = open(user_ascii_path, "r").read()
        pc_ascii_path = os.path.join(self.ascii_path, f"{pc_hand}.txt")
        pc_ascii = open(pc_ascii_path, "r").read()
        print(f"You chose: {user_hand}")
        print(user_ascii)
        print(f"Computer chose: {pc_hand}")
        print(pc_ascii)

    def print_outcome(self, result):
        if result == "win":
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("It's a draw!")

    def update_score(self, result):
        if result == "win":
            self.score["user"] += 1
        elif result == "loss":
            self.score["pc"] += 1

    def print_score(self):
        print(f"You: {self.score['user']} || PC: {self.score['pc']}")

    def prepare_hands(self, preset_hand):

        user_choice = input(self.instructions())
        if user_choice.lower() == "q":
            return ["quit", None]

        user_hand = self.find_key_by_code(int(user_choice))

        if user_hand is None:
            print(f"USER HAND: {user_choice} --> {user_hand}")
            print("This option does not exist.")
            return [None, None]

        if preset_hand is None:
            random_hand = random.choice(list(self.rules.keys()))

        pc_hand = preset_hand or random_hand

        return [user_hand, pc_hand]

    def update_screen(self, result, user_hand, pc_hand):
        self.update_score(result)
        self.print_hands(user_hand, pc_hand)
        self.print_outcome(result)
        self.print_score()

    def declare_winner(self):
        msg = {
            self.score["user"] > self.score["pc"]: "You won the game!",
            self.score["user"] < self.score["pc"]: "The computer won the game!",
        }.get(True, "It's a draw!")

        print(msg)

    def initial_game_values(self):
        current_result = None
        counter = 0
        running = True
        return [current_result, counter, running]

    def start_screen(self):
        os.system("clear")
        self.print_score()
        print(f"ROUNDS: { self.rounds}")

    def play_single_round(
        self, preset_hand, current_result, counter, running, single_round
    ):
        user_hand, pc_hand = self.prepare_hands(preset_hand)
        os.system("clear")
        #
        if user_hand is None and single_round:
            print("This option does not exist.  Thanks for playing!")
            return

        if user_hand is None:
            print("This option does not exist.")
            return

        if user_hand == "quit":
            print("Thanks for playing!")
            return current_result

        result = self.play_round(user_hand, pc_hand)
        current_result = result

        self.update_screen(result, user_hand, pc_hand)

        counter += 1
        print(f"COUNTER: {counter}, ROUNDS: {self.rounds}")
        if counter == self.rounds or single_round:
            self.declare_winner()
            print("Thanks for playing!")
            return current_result

    def play(self, preset_hand=None, single_round=False):

        self.start_screen()
        current_result, counter, running = self.initial_game_values()

        while running:
            self.play_single_round(preset_hand, single_round, *self.initial_game_values())
            # user_hand, pc_hand = self.prepare_hands(preset_hand)
            # os.system("clear")
            # #
            # if user_hand is None and single_round:
            #     print("This option does not exist.  Thanks for playing!")
            #     return
            #
            # if user_hand is None:
            #     print("This option does not exist.")
            #     continue
            #
            # if user_hand == "quit":
            #     print("Thanks for playing!")
            #     return current_result
            #
            # result = self.play_round(user_hand, pc_hand)
            # current_result = result
            #
            # self.update_screen(result, user_hand, pc_hand)
            #
            # counter += 1
            # print(f"COUNTER: {counter}, ROUNDS: {self.rounds}")
            # if counter == self.rounds or single_round:
            #     self.declare_winner()
            #     print("Thanks for playing!")
            #     return current_result

        return current_result


def main():
    if len(sys.argv) > 1 and isinstance(int(sys.argv[1]), int):
        new_game = Game(int(sys.argv[1]))
    else:
        new_game = Game()

    new_game.play()


if __name__ == "__main__":
    main()
