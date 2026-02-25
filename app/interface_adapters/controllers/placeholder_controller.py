from app.application.usecases.placeholder_usecase import PlaceholderUseCase
from app.interface_adapters.schemas.placeholder_schema import (
    PlaceholderRequest,
    PlaceholderResponse,
)


class PlaceholderController:
    """Adapts HTTP input to the application use-case and formats the output."""

    def __init__(self, use_case: PlaceholderUseCase) -> None:
        self._use_case = use_case

    def handle(self, request: PlaceholderRequest) -> PlaceholderResponse:
        result = self._use_case.execute(name=request.name)
        return PlaceholderResponse(**result)
