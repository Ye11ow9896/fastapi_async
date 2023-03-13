from sqlalchemy.ext.asyncio import AsyncSession
from components.product.models import Products
from sqlalchemy.future import select


class ProductDAL:
    """Data Access Layer for creating user info"""
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_product(
            self, name: str, link: str, ave_price: float
    ) -> Products:
        new_product = Products(
            name=name,
            link=link,
            ave_price=ave_price
        )
        self.db.add(new_product)
        await self.db.flush()
        return new_product

    async def show_all_products(self) -> Products:
        query = select(Products)
        products = await self.db.execute(self, query)
        return products

