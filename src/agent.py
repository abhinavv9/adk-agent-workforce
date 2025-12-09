import google
from google.generativeai.types import ToolConfig

class GreetingAgent:
    """An agent that can greet users."""

    def greet(self, name: str) -> str:
        """Greets the user by name."""
        return f"Hello, {name}!"
