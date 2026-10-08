from pydantic import BaseModel

from modules.risk_scoring.schemas.risk_event_response import RiskEventResponse


class RiskScoreResponse(BaseModel):
    score: float
    risk_level: str
    model_version: str
    risk_events: list[RiskEventResponse]