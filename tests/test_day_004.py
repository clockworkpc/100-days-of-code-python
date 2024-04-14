#!/usr/bin/env python

"""Tests for `day_004` package."""

from src.days_of_code import day_004 as d
import pytest

# open(ascii_path, "r").read()

# rps_folder_path = os.path.join(os.getcwd(), "src", "days_of_code", "assets", "ascii")
# rock_ascii_path = os.path.join(rps_folder_path, "rock.txt")
# paper_ascii_path = os.path.join(rps_folder_path, "paper.txt")
# scissors_ascii_path = os.path.join(rps_folder_path, "scissors.txt")
#
# rock_ascii = open(rock_ascii_path, "r").read()
# paper_ascii = open(paper_ascii_path, "r").read()
# scissors_ascii = open(scissors_ascii_path, "r").read()
#


@pytest.fixture
def game():
    yield d.Game()


# def test_ascii(game):
#     assert game.ascii["rock"] == rock_ascii
#     assert game.ascii["paper"] == paper_ascii
#     assert game.ascii["scissors"] == scissors_ascii


def test_rules_keys(game):
    my_list = list(game.rules.keys())
    assert my_list == ["rock", "paper", "scissors"]


def test_rules_rock(game):
    result = game.rules["rock"]["results"]["rock"]
    assert result == "draw"
    result = game.rules["rock"]["results"]["paper"]
    assert result == "loss"
    result = game.rules["rock"]["results"]["scissors"]
    assert result == "win"


def test_rules_paper(game):
    result = game.rules["paper"]["results"]["rock"]
    assert result == "win"
    result = game.rules["paper"]["results"]["paper"]
    assert result == "draw"
    result = game.rules["paper"]["results"]["scissors"]
    assert result == "loss"


def test_rules_scissors(game):
    result = game.rules["scissors"]["results"]["rock"]
    assert result == "loss"
    result = game.rules["scissors"]["results"]["paper"]
    assert result == "win"
    result = game.rules["scissors"]["results"]["scissors"]
    assert result == "draw"


def test_play_round_rock(game):
    result = game.play_round("rock", "rock")
    assert result == "draw"
    result = game.play_round("rock", "paper")
    assert result == "loss"
    result = game.play_round("rock", "scissors")
    assert result == "win"


def test_play_round_paper(game):
    result = game.play_round("paper", "rock")
    assert result == "win"
    result = game.play_round("paper", "paper")
    assert result == "draw"
    result = game.play_round("paper", "scissors")
    assert result == "loss"


def test_play_round_scissors(game):
    result = game.play_round("scissors", "rock")
    assert result == "loss"
    result = game.play_round("scissors", "paper")
    assert result == "win"
    result = game.play_round("scissors", "scissors")
    assert result == "draw"


# def test_play_rock(game):
#     monkeypatch = pytest.MonkeyPatch()
#     inputs = iter(["rock"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     result = game.play("rock")
#     assert result == "draw"


def play_test(game, hand1, hand2, expectation):
    monkeypatch = pytest.MonkeyPatch()
    inputs = iter([hand1])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = game.play(hand2)
    assert result == expectation


def test_play_rock(game):
    play_test(game, "0", "rock", "draw")
    play_test(game, "0", "paper", "loss")
    play_test(game, "0", "scissors", "win")


def test_play_paper(game):
    play_test(game, "1", "rock", "win")
    play_test(game, "1", "paper", "draw")
    play_test(game, "1", "scissors", "loss")


def test_play_scissors(game):
    play_test(game, "2", "rock", "loss")
    play_test(game, "2", "paper", "win")
    play_test(game, "2", "scissors", "draw")


# @pytest.fixture
# def scenes():
#     game = d.Game()
#     yield game.scenes
#
#
# def test_json(scenes):
#     assert scenes["s1"]["choices"][0]["choice"] == "left"
#
#
# def individual_scenario_test(scenes, scene_key, input_list, expectation):
#     monkeypatch = pytest.MonkeyPatch()
#     inputs = iter(input_list)
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     scene = scenes[scene_key]
#     game = d.Game()
#     result = game.scenario(scene)
#     assert result is expectation
#
#
# def scenario_sequence_test(scenes, hsh, expectation):
#     monkeypatch = pytest.MonkeyPatch()
#     input_list = list(hsh.values())
#     inputs = iter(input_list)
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     game = d.Game()
#     result = game.play()
#     assert result == expectation
#
#
# def test_scenario1(scenes):
#     individual_scenario_test(scenes, "s1", ["left"], True)
#     individual_scenario_test(scenes, "s1", ["right"], False)
#     individual_scenario_test(scenes, "s1", ["foo"], False)
#
#
# def test_sequence1(scenes):
#     message = "Fall into a hole.\nGame over."
#     scenario_sequence_test(scenes, {"s1": "right"}, message)
#     scenario_sequence_test(scenes, {"s1": "foo"}, message)
#
#
# def test_scenario2(scenes):
#     individual_scenario_test(scenes, "s2", ["wait"], True)
#     individual_scenario_test(scenes, "s2", ["swim"], False)
#     individual_scenario_test(scenes, "s2", ["foo"], False)
#
#
# def test_sequence2(scenes):
#     message = "Attacked by trout.\nGame over."
#     scenario_sequence_test(scenes, {"s1": "left", "s2": "swim"}, message)
#     scenario_sequence_test(scenes, {"s1": "left", "s2": "foo"}, message)
#
#
# def test_scenario3(scenes):
#     individual_scenario_test(scenes, "s3", ["yellow"], True)
#     individual_scenario_test(scenes, "s3", ["red"], False)
#     individual_scenario_test(scenes, "s3", ["blue"], False)
#     individual_scenario_test(scenes, "s3", ["foo"], False)
#
#
# def test_sequence3(scenes):
#     sequence3a = {"s1": "left", "s2": "wait", "s3": "red"}
#     message1 = "Burned by fire.\nGame over."
#     scenario_sequence_test(scenes, sequence3a, message1)
#
#     sequence3b = {"s1": "left", "s2": "wait", "s3": "blue"}
#     message2 = "Eaten by beasts.\nGame over."
#     scenario_sequence_test(scenes, sequence3b, message2)
#
#     sequence3c = {"s1": "left", "s2": "wait", "s3": "yellow"}
#     message3 = "You win!"
#     scenario_sequence_test(scenes, sequence3c, message3)
#
#     message4 = "Game over."
#     scenario_sequence_test(scenes, {"s1": "left", "s2": "wait", "s3": "foo"}, message4)
