"""Day 7: Hangman"""

import json
import os
import glob
import random


class Hangman:
    """Classic Hangman game"""

    def __init__(self, lives=None):
        assets_ary = "src/days_of_code/assets/hangman".split("/")
        self.assets_path = os.path.join(os.getcwd(), *assets_ary)
        self.logo = self.load_logo()
        self.words = self.load_words()
        self.stages = self.load_stages()
        self.lives = lives or 6
        self.display = None

    def print_stage(self, key):
        file = open(self.stages[key], "r").read()
        print(file)
        self.print_msg("lives_left", self.lives)
        return file

    def load_logo(self):
        logo_path = os.path.join(self.assets_path, "logo.txt")
        return open(logo_path, "r").read()

    def load_words(self):
        words_path = os.path.join(self.assets_path, "words.json")
        return json.load(open(words_path, "r"))

    def load_stages(self):
        stages = {}
        pattern = os.path.join(self.assets_path, "stage*.txt")
        sorted_paths = sorted(glob.glob(pattern), key=lambda x: os.path.basename(x))
        for index, path in enumerate(sorted_paths):
            stages[index] = path
        return stages

    def print_msg(self, key, guess=None):
        msg = {
            "input": "Guess a letter: ",
            "already_guessed": "You've already guessed {}",
            "wrong_guess": "You guessed {}, that's not in the word. You lose a life.",
            "game_over": "You lose.",
            "lives_left": "You have {} lives left.",
        }

        if key not in msg.keys():
            return

        if guess and isinstance(guess, (int, float)):
            guess = str(guess)

        message = msg[key].format(guess) if guess else msg[key]
        print(message)
        return message

    def title_screen(self):
        os.system("clear")
        print(self.logo)
        self.print_stage(self.lives)

    def choose_word(self):
        word = random.choice(self.words)
        self.display = ["_" for _ in range(len(word))]
        return word

    def check_guess(self, word, guess):
        if guess in self.display:
            self.print_msg("already_guessed", guess)
            return None

        for n in range(len(word)):
            letter = word[n]

            if letter == guess:
                self.display[n] = letter
                return True

        if guess not in word:
            self.lives -= 1
            self.print_msg("wrong_guess", guess)
            return False

    def guess_letter(self):
        raw_input = input("Guess a letter: ").lower()
        # Ensure that guess can only be one lower case letter
        return list(set([c for c in raw_input]))[0]

    def is_game_over(self, word):
        if self.lives == 0:
            print("You lose!")
            print(f"The word was **{word}**")

            return True

        if "_" not in self.display:
            print("You win!")
            return True

        return False

    def update_screen(self):
        os.system("clear")
        print("THE SECRET WORD")
        print(f"{' '.join(self.display)}\n")
        self.print_stage(self.lives)

    def play(self):
        self.title_screen()
        word = self.choose_word()
        running = True
        while running:
            guess = self.guess_letter()
            self.check_guess(word, guess)
            self.update_screen()

            if self.is_game_over(word):
                running = False
                print("Thanks for playing!")


def main():
    g = Hangman()
    g.play()


if __name__ == "__main__":
    main()
