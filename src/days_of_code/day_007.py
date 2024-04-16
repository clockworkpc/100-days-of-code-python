"""Day 7: Hangman"""

import json
import os
import glob


class Hangman:
    """Classic Hangman game"""

    def __init__(self, lives=None):
        assets_ary = "src/days_of_code/assets/hangman".split("/")
        self.assets_path = os.path.join(os.getcwd(), *assets_ary)
        self.logo = self.load_logo()
        self.words = self.load_words()
        self.stages = self.load_stages()
        self.lives = lives or 6

    def print_stage(self, key):
        file = open(self.stages[key], "r").read()
        print(file)
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

    def title_screen(self):
        print(self.logo)

    def play():
        chosen_word = random.choice(self.words)
        word_length = len(chosen_word)
        self.title_screen()
