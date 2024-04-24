"""Day 55: Decorator Function Exercise"""

import random


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


class Admin(User):
    def __init__(self, name):
        super().__init__(name)


class Post:
    def __init__(self, id=None):
        self.id = id or random.randint(0, 1000)


def is_authenticated(function):
    def wrapper(*args):
        if args[0].is_logged_in is True:
            return function(*args)
        else:
            raise Exception("401")

    return wrapper


def is_admin(function):
    def wrapper(*args, **kwargs):
        if isinstance(args[0], Admin):
            return function(*args, **kwargs)
        else:
            raise Exception("401")

    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
    return {"status": "ok"}


@is_admin
@is_authenticated
def delete_blog_post(user, post):
    print(f"{user.name} deleted post {post.id}")
    return {"status": "ok"}
