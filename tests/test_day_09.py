#!/usr/bin/env python

"""Tests for `day_09` package."""

from src.days_of_code import day_09 as d
import pytest


@pytest.fixture
def auction():
    yield d.Auction()


@pytest.mark.parametrize("hsh,expected", [({"foo": 123}, {"status": "ok", "foo": 123})])
def test_bid(auction, hsh, expected):
    assert auction.bid(hsh) == expected


@pytest.fixture
def bids0():
    return {"foo": 100, "bar": 150, "fizz": 200, "bang": 250}


@pytest.fixture
def bids1():
    return {"foo": 450, "bar": 400, "fizz": 350, "bang": 300}


@pytest.mark.parametrize("bids_fixture, expected", [("bids0", "bang"), ("bids1", "foo")])
def test_find_highest_bidder(request, auction, bids_fixture, expected):
    my_bids = request.getfixturevalue(bids_fixture)
    auction.batch_bids(my_bids)
    assert auction.find_highest_bidder() == expected


@pytest.fixture
def auction1(bids0):
    a = d.Auction()
    a.batch_bids(bids0)
    yield a


@pytest.mark.filter
@pytest.mark.parametrize(
    "bid, status",
    [
        ({"foo": 50}, {"status": "rejected"}),
        ({"bar": 100}, {"status": "rejected"}),
        ({"boom": 250}, {"status": "rejected"}),
    ],
)
def test_insufficient_bid(auction1, bid, status):
    expectation = {**bid, **status}
    assert auction1.bid(bid) == expectation


def test_no_bids_yet(auction):
    assert auction.bids == {}
