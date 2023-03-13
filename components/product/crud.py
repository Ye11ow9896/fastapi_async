from components.product import schemas
from components.product.dal import ProductDAL
from db.db import async_session


async def create_new_product(body: schemas.CreateProduct):
    async with async_session() as session:
        async with session.begin():
            product_dal = ProductDAL(session)
            product = await product_dal.create_product(
                name=body.name,
                link=body.link,
                ave_price=body.ave_price
            )
            return schemas.ShowProduct(
                id=product.id,
                name=product.name,
                link=product.link,
                ave_price=product.ave_price
            )


async def show_all_products():
    async with async_session() as session:
        async with session.begin():
            product_dal = ProductDAL(session)
            product = await product_dal.show_all_products()
            return schemas.ShowProduct(
                id=product.id,
                name=product.name,
                link=product.link,
                ave_price=product.ave_price
            )

