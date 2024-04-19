"""Day 4: Rock Paper Scissors"""

import os
import sys
import json
import random


class Game:

    def __init__(self, rounds=5):
        assets_ary = "src/days_of_code/assets".split("/")
        self.ascii_path = os.path.join(os.getcwd(), *assets_ary, "ascii")
        json_ary = assets_ary + "json/day_04_rules.json".split("/")
        json_path = os.path.join(os.getcwd(), *json_ary)
        self.rules = json.load(open(json_path, "r"))
        self.score = {"user": 0, "pc": 0}
        self.rounds = rounds
        self.counter = 0

    def consult_the_rules(self, hand1, hand2):
        return self.rules[hand1]["results"][hand2]

    def prepare_hands(self, preset_hand):
        def instructions():
            options_ary = []
            for k, v in self.rules.items():
                options_ary.append(f"{v['code']} for {k.capitalize()}")
            options_ary.append("Q for Quit")

            return " ".join(["Type", ", ".join(options_ary), "\nYour choice: "])

        def find_hand_by_code(target_code):
            for key, value in self.rules.items():
                if value["code"] == target_code:
                    return key
            return None

        user_choice = input(instructions())

        if user_choice.lower() == "q":
            print("You QUIT")
            return ["quit", None]

        user_hand = find_hand_by_code(int(user_choice))

        if user_hand is None:
            print(f"USER HAND: {user_choice} --> {user_hand}")
            print("This option does not exist.")
            return [None, None]

        if preset_hand is None:
            random_hand = random.choice(list(self.rules.keys()))

        pc_hand = preset_hand or random_hand

        return [user_hand, pc_hand]

    def print_score(self):
        print(f"You: {self.score['user']} || PC: {self.score['pc']}")

    def update_screen(self, result, user_hand, pc_hand):

        def update_score(result):
            if result == "win":
                self.score["user"] += 1
            elif result == "loss":
                self.score["pc"] += 1

        def print_hands(user_hand, pc_hand):
            user_ascii_path = os.path.join(self.ascii_path, f"{user_hand}.txt")
            user_ascii = open(user_ascii_path, "r").read()
            pc_ascii_path = os.path.join(self.ascii_path, f"{pc_hand}.txt")
            pc_ascii = open(pc_ascii_path, "r").read()
            print(f"You chose: {user_hand}")
            print(user_ascii)
            print(f"Computer chose: {pc_hand}")
            print(pc_ascii)

        def print_outcome(result):
            if result == "win":
                print("You win!")
            elif result == "loss":
                print("You lose!")
            else:
                print("It's a draw!")

        update_score(result)
        print_hands(user_hand, pc_hand)
        print_outcome(result)
        self.print_score()

    def start_screen(self):
        os.system("clear")
        self.print_score()
        print(f"ROUNDS: { self.rounds}")

    def play_round(self, preset_hand, current_result):
        user_hand, pc_hand = self.prepare_hands(preset_hand)
        os.system("clear")

        if user_hand is None:
            print("This option does not exist.")
            return current_result

        if user_hand == "quit":
            # print("Thanks for playing!")
            self.counter = self.rounds
            return current_result

        result = self.consult_the_rules(user_hand, pc_hand)
        self.update_screen(result, user_hand, pc_hand)

        self.counter += 1

        return result

    def declare_winner(self):
        msg = {
            self.score["user"] > self.score["pc"]: "You won the game!",
            self.score["user"] < self.score["pc"]: "The computer won the game!",
        }.get(True, "No-one won the game!")

        print(msg)
        print("Thanks for playing!")

    def play(self, preset_hand=None):

        self.start_screen()
        current_result = None

        running = True
        while running:
            current_result = self.play_round(preset_hand, current_result)

            if self.counter == self.rounds:
                self.declare_winner()
                return current_result

        return current_result


def main():
    if len(sys.argv) > 1 and isinstance(int(sys.argv[1]), int):
        new_game = Game(int(sys.argv[1]))
    else:
        new_game = Game()

    new_game.play()


if __name__ == "__main__":
    main()
