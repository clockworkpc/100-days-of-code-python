#!/usr/bin/env python

"""Tests for `day_004` package."""

from src.days_of_code import day_004 as d
import pytest


@pytest.fixture
def game():
    yield d.Game()


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


def play_test(game, hand1, hand2, expectation):
    monkeypatch = pytest.MonkeyPatch()
    inputs = iter([hand1])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = game.play(hand2, True)
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


def test_play_error(game):
    play_test(game, "3", "rock", None)
