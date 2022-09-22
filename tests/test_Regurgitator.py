import pytest

from app.regurgitator import Regurgitator

@pytest.fixture
def regurgitate():

    return Regurgitator()

def test_init(regurgitate):

    assert regurgitate.initiated

def test_hello(regurgitate):

    assert regurgitate.hello("Mark") == "Hello, Mark!"
