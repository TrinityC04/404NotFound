from fastapi import APIRouter

from modules.kyc.application.kyc_service import KycService

router = APIRouter(
    prefix="/kyc",
    tags=["KYC"]
)

service = KycService()


@router.get("/{customer_id}")
async def get_kyc(customer_id: str):
    return await service.get_customer_kyc(customer_id)