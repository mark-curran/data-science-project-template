"""Tests for the Regurgitator class."""


def test_init(fixture_regurgitator):
    """Test Regurgitator init.

    Args:
        fixture_regurgitator (Regurgitator): Initialized Regurgitator.
    """
    assert fixture_regurgitator.initiated


def test_hello(fixture_regurgitator):
    """Test Regurgitator.hello method.

    Args:
        fixture_regurgitator (Regurgitator): Initialized Regurgitator.
    """
    assert fixture_regurgitator.hello("Bob") == "Hello, Bob!"


def test_goodbye(fixture_regurgitator):
    """Test Regurgitator.goodbye method.

    Args:
        fixture_regurgitator (Regurgitator): Initialized Regurgitator.
    """
    assert fixture_regurgitator.goodbye("Sally") == "Goodbye, Sally :("
