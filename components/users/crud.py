import schemas
from db.db import async_session
from main import UserDAL


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
                user_id=user.user_id,
                name=user.name,
                email=user.email,
                is_active=user.is_active,
            )


