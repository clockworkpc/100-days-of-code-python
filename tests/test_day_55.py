#!/usr/bin/env python

"""Tests for `day_55` package."""

from src.days_of_code import day_55 as d
import pytest


@pytest.fixture
def user_with_login():
    u = d.User("Foo")
    u.is_logged_in = True
    yield u


@pytest.fixture
def user_sans_login():
    u = d.User("Bar")
    print(u.name)
    print(u.is_logged_in)
    yield u


@pytest.fixture
def admin_with_login():
    u = d.Admin("MyAdmin")
    u.is_logged_in = True
    yield u


@pytest.fixture
def my_post():
    post = d.Post(42)
    yield post


@pytest.mark.filter
def test_authenticated(user_with_login):
    assert user_with_login.is_logged_in is True
    assert d.create_blog_post(user_with_login) == {"status": "ok"}


@pytest.mark.filter
def test_unauthenticated(user_sans_login):
    assert user_sans_login.is_logged_in is False
    with pytest.raises(Exception) as e:
        assert d.create_blog_post(user_sans_login) == {"status": "ok"}
        assert e.value == "401"


@pytest.mark.filter
def test_authenticated_admin(admin_with_login, my_post):
    assert admin_with_login.is_logged_in is True
    assert isinstance(admin_with_login, d.Admin) is True
    assert my_post.id == 42
    assert d.delete_blog_post(admin_with_login, my_post) == {"status": "ok"}
