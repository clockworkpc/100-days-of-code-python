#!/usr/bin/env python

"""Tests for `day_07` package."""

from src.days_of_code import day_07 as d
import pytest

# import json
# import os
# import re


@pytest.fixture
def game():
    yield d.Hangman()


def test_logo(game):
    res = game.logo
    print(res)


def test_words(game):
    res = game.words
    print(res)


def test_stages(game):
    for i in range(0, 7):
        game.print_stage(i)


@pytest.mark.filter
def test_print_msg(game):
    res = game.print_msg("lives_left", game.lives)
    assert res == "You have 6 lives left."