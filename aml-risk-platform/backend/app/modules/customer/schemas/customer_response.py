from uuid import UUID
from pydantic import BaseModel


class CustomerResponse(BaseModel):
    customer_id: UUID
    first_name: str
    last_name: str
    country: str
    customer_status: str