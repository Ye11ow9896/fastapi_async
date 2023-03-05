from components.users import schemas
from components.users.dal import UserDAL
from db.db import async_session


async def create_new_user(body: schemas.UserCreate) -> schemas.ShowUser:
    async with async_session() as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name,
                surname=body.surname,
                email=body.email
            )
            return schemas.ShowUser(
                id=user.id,
                name=user.name,
                surname=user.surname,
                email=user.email,
                is_active=user.is_active,
            )





