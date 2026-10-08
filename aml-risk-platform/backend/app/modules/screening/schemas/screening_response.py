from pydantic import BaseModel


class ScreeningResponse(BaseModel):
    screening_type: str
    result: str
    match_found: bool
    matched_entity: str | None = None