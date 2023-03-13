from fastapi import APIRouter
from components.users import (schemas, crud)

router = APIRouter(prefix='/user', tags=['user'])


@router.post("/")
async def create_user(body: schemas.UserCreate) -> schemas.ShowUser:
    return await crud.create_new_user(body=body)

