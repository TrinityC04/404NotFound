from modules.customer.infrastructure.customer_repository import CustomerRepository


class CustomerService:

    def __init__(self):
        self.repository = CustomerRepository()

    async def get_customer(self, customer_id: str):
        return await self.repository.get_by_id(customer_id)