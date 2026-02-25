class AppException(Exception):
    """Infrastructure-level exception that carries an HTTP status code."""

    def __init__(
        self,
        message: str = "An unexpected error occurred",
        code: str = "APP_ERROR",
        status_code: int = 500,
    ):
        self.message = message
        self.code = code
        self.status_code = status_code
        super().__init__(self.message)
