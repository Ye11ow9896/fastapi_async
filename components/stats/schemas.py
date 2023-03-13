import re
import uuid

from fastapi import HTTPException
from pydantic import BaseModel


LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):

    class Config:
        orm_mode = True


class AddStats(BaseModel):
    product_id: int
    price: float


class ShowStats(TunedModel):
    id: int
    product_id: int
    date: str
    price: float

