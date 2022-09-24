import pytest

from app.regurgitator import Regurgitator


@pytest.fixture
def regurgitate():

    return Regurgitator()


def test_init(regurgitate):

    assert regurgitate.initiated


def test_hello(regurgitate):

    assert regurgitate.hello("Bob") == "Hello, Bob!"


def test_goodbye(regurgitate):

    print("hello")
