import uuid
import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, UUID, Numeric, TIMESTAMP
from db.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class Products(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    link = Column(String, nullable=False)
    ave_price = (Numeric(2, 7))


class Stats(Base):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    priduct_id = Column(Integer, ForeignKey('product.id'))
    date = Column(TIMESTAMP, nullable=False, default=datetime.date.today())
    price = Column(Numeric(2, 7), nullable=False)

