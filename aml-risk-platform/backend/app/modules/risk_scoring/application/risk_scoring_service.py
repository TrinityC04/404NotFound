from modules.risk_scoring.infrastructure.risk_scoring_repository import (
    RiskScoringRepository,
)


class RiskScoringService:

    def __init__(self):
        self.repository = RiskScoringRepository()

    async def calculate(self, customer_id: str):

        score = 15

        risk_events = []

        score += 25

        risk_events.append({
            "risk_category": "KYC",
            "risk_type": "KYC_PENDING",
            "contribution": 25,
            "description": "Customer KYC not completed"
        })

        score += 30

        risk_events.append({
            "risk_category": "SCREENING",
            "risk_type": "PEP_MATCH",
            "contribution": 30,
            "description": "Customer matched PEP list"
        })

        return {
            "score": score,
            "risk_level": "HIGH",
            "model_version": "1.0",
            "risk_events": risk_events
        }