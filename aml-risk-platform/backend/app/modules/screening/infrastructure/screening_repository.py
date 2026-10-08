class ScreeningRepository:

    async def get_customer_screening(self, customer_id: str):

        return [
            {
                "screening_type": "PEP",
                "result": "CLEAR",
                "match_found": False,
                "matched_entity": None
            }
        ]