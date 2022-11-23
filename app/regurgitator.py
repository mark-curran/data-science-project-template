"""A class that echoes string inputs."""


class Regurgitator:
    """A Class that regurgitates strings."""

    def __init__(self):
        """Initialize the class."""
        self.initiated = True

    def hello(self, name: str) -> str:
        """Prepend 'Hello, ' to the argument name.

        Args:
            name (str): Will be appended to 'Hello, '.

        Returns:
            str: 'Hello, ' followed by name.
        """
        return f"Hello, {name}!"

    def goodbye(self, name: str) -> str:
        """Prepend 'Goodbye, ' to the argument name, append ' :('.

        Args:
            name (str): Inserted between 'Goodbye, ' and ' :('.

        Returns:
            str: Goodbye, name and :( concatenated together.
        """
        return f"Goodbye, {name} :("
