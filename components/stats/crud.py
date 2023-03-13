from components.stats import schemas
from components.stats.dal import StatsDAL
from db.db import async_session


async def add_new_stat(body: schemas.AddStats) -> schemas.ShowStats:
    async with async_session() as session:
        async with session.begin():
            stat_dal = StatsDAL(session)
            stat = await stat_dal.add_stat(
                product_id=body.product_id,
                price=body.price
            )
            return schemas.ShowStats(
                id=stat.id,
                product_id=stat.product_id,
                date=stat.date,
                price=stat.price
            )

