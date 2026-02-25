class MessagePattern:
    """Encapsulates the formatting rule for greeting messages."""

    TEMPLATE = "Hello {name}, this is a clean architecture placeholder."

    @staticmethod
    def format(name: str) -> str:
        return MessagePattern.TEMPLATE.format(name=name)
