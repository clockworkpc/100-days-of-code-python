#!/usr/bin/env python

"""Tests for `day_04` package."""

from src.days_of_code import day_04 as d
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
    result = game.consult_the_rules("rock", "rock")
    assert result == "draw"
    result = game.consult_the_rules("rock", "paper")
    assert result == "loss"
    result = game.consult_the_rules("rock", "scissors")
    assert result == "win"


def test_play_round_paper(game):
    result = game.consult_the_rules("paper", "rock")
    assert result == "win"
    result = game.consult_the_rules("paper", "paper")
    assert result == "draw"
    result = game.consult_the_rules("paper", "scissors")
    assert result == "loss"


def test_play_round_scissors(game):
    result = game.consult_the_rules("scissors", "rock")
    assert result == "loss"
    result = game.consult_the_rules("scissors", "paper")
    assert result == "win"
    result = game.consult_the_rules("scissors", "scissors")
    assert result == "draw"


def single_play_test(rounds, hand1, hand2, expectation):
    game = d.Game(rounds)
    monkeypatch = pytest.MonkeyPatch()
    inputs = iter([hand1])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = game.play(hand2)
    assert result == expectation


def test_play_rock(game):
    single_play_test(1, "0", "rock", "draw")
    single_play_test(1, "0", "paper", "loss")
    single_play_test(1, "0", "scissors", "win")


def test_play_paper(game):
    single_play_test(1, "1", "rock", "win")
    single_play_test(1, "1", "paper", "draw")
    single_play_test(1, "1", "scissors", "loss")


def test_play_scissors(game):
    single_play_test(1, "2", "rock", "loss")
    single_play_test(1, "2", "paper", "win")
    single_play_test(1, "2", "scissors", "draw")


def test_play_error(game):
    single_play_test(0, "3", "rock", None)
