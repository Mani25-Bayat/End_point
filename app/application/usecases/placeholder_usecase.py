from app.application.services.greeting_service import GreetingService


class PlaceholderUseCase:
    """Orchestrates the placeholder greeting scenario."""

    def __init__(self, greeting_service: GreetingService) -> None:
        self._greeting_service = greeting_service

    def execute(self, name: str) -> dict[str, str]:
        message = self._greeting_service.greet(name)
        return {"message": message}
