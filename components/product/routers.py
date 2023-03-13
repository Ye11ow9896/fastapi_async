from fastapi import APIRouter
from components.product import (schemas, crud)

product_router = APIRouter(prefix='/product', tags=['product'])


@product_router.post("/create")
async def create(body: schemas.CreateProduct) -> schemas.ShowProduct:
    return await crud.create_new_product(body=body)


@product_router.get('/show_all')
async def show_all() -> list[schemas.ShowProduct]:
    return await crud.show_all_products()

