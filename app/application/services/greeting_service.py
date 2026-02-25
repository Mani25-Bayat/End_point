from app.application.patterns.message_pattern import MessagePattern
from app.application.exceptions.domain_exception import InvalidNameException


class GreetingService:
    """Domain service responsible for producing greeting messages."""

    def __init__(self) -> None:
        self._pattern = MessagePattern()

    def greet(self, name: str) -> str:
        cleaned = name.strip()
        if not cleaned:
            raise InvalidNameException()
        return self._pattern.format(cleaned)
