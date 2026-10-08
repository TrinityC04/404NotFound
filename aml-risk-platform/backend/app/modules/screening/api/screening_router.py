from fastapi import APIRouter

from modules.screening.application.screening_service import ScreeningService

router = APIRouter(
    prefix="/screening",
    tags=["Screening"]
)

service = ScreeningService()


@router.get("/{customer_id}")
async def get_screening(customer_id: str):
    return await service.get_customer_screening(customer_id)