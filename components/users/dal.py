from sqlalchemy.ext.asyncio import AsyncSession
from components.users.models import User


class UserDAL:
    """Data Access Layer for creating user info"""
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(
            self, name: str, surname: str, email: str
    ) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email,
        )
        self.db.add(new_user)
        await self.db.flush()
        return new_user

