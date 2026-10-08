from pydantic import BaseModel


class KycResponse(BaseModel):
    identity_status: str
    address_status: str
    verification_result: str