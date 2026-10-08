class CustomerRepository:

    async def get_by_id(self, customer_id: str):

        return {
            "customer_id": customer_id,
            "first_name": "John",
            "last_name": "Doe",
            "country": "ZA",
            "customer_status": "ACTIVE"
        }