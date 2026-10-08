class KycRepository:

    async def get_customer_kyc(self, customer_id: str):

        return {
            "identity_status": "VERIFIED",
            "address_status": "VERIFIED",
            "verification_result": "PASS"
        }