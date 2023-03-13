from fastapi import APIRouter

from components.stats import (schemas, crud)

stat_router = APIRouter(prefix='/stat', tags=['stat'])


@stat_router.post('/add')
async def add_stat(body: schemas.AddStats) -> schemas.ShowStats:
    return await crud.add_new_stat(body=body)

