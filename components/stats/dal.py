from sqlalchemy.ext.asyncio import AsyncSession
from components.stats.models import Stats


class StatsDAL:
    """Data Access Layer for creating user info"""
    def __init__(self, db: AsyncSession):
        self.db = db

    async def add_stat(
            self, product_id, price):
        new_stat = Stats(
            priduct_id=product_id,
            price=price
        )
        self.db.add(new_stat)
        await self.db.flush()
        return new_stat

