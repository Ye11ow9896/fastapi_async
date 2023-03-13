from sqlalchemy import Column, Integer, String, Numeric
from db.db import Base


class Products(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    link = Column(String, nullable=False)
    ave_price = (Numeric(2, 7))

