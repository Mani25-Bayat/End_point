class DomainException(Exception):
    """Base exception for all domain/business-rule violations."""

    def __init__(self, message: str = "A domain error occurred", code: str = "DOMAIN_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)


class InvalidNameException(DomainException):
    """Raised when the provided name is empty or invalid."""

    def __init__(self, message: str = "Name must not be empty"):
        super().__init__(message=message, code="INVALID_NAME")
