"""Fixtures for tests."""
import pytest

from app.regurgitator import Regurgitator


@pytest.fixture
def fixture_regurgitator() -> Regurgitator:
    """Fixture for the Regurgitator class.

    Returns:
        Regurgitator: Initialized Regurgitator class.
    """
    return Regurgitator()
