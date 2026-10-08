from fastapi import APIRouter

from modules.customer.application.customer_service import CustomerService

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

service = CustomerService()


@router.get("/{customer_id}")
async def get_customer(customer_id: str):
    return await service.get_customer(customer_id)