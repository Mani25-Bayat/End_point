from pydantic import BaseModel, Field


class PlaceholderRequest(BaseModel):
    name: str = Field(..., min_length=1, examples=["Farnoosh"])


class PlaceholderResponse(BaseModel):
    message: str = Field(..., examples=["Hello Farnoosh, this is a clean architecture placeholder."])
