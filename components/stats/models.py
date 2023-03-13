import datetime
from sqlalchemy import Column, ForeignKey, Integer, Numeric, TIMESTAMP
from db.db import Base
from components.product.models import Products


class Stats(Base):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'))
    date = Column(TIMESTAMP, nullable=False, default=datetime.date.today())
    price = Column(Numeric(7, 2), nullable=False)

