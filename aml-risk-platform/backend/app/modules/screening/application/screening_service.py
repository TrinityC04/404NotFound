from modules.screening.infrastructure.screening_repository import ScreeningRepository


class ScreeningService:

    def __init__(self):
        self.repository = ScreeningRepository()

    async def get_customer_screening(self, customer_id: str):
        return await self.repository.get_customer_screening(customer_id)