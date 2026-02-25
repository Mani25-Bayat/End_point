from fastapi import APIRouter, Depends

from app.interface_adapters.schemas.placeholder_schema import (
    PlaceholderRequest,
    PlaceholderResponse,
)
from app.interface_adapters.controllers.placeholder_controller import PlaceholderController
from app.application.usecases.placeholder_usecase import PlaceholderUseCase
from app.application.services.greeting_service import GreetingService

router = APIRouter(prefix="/placeholder", tags=["Placeholder"])


def _get_controller() -> PlaceholderController:
    service = GreetingService()
    use_case = PlaceholderUseCase(greeting_service=service)
    return PlaceholderController(use_case=use_case)


@router.post(
    "",
    response_model=PlaceholderResponse,
    summary="Placeholder greeting",
    description="Returns a greeting message built with clean architecture layers.",
)
async def create_placeholder(
    body: PlaceholderRequest,
    controller: PlaceholderController = Depends(_get_controller),
) -> PlaceholderResponse:
    return controller.handle(body)
