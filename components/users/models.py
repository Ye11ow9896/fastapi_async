import uuid
import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Numeric, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from db.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

