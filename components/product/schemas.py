import re
import uuid

from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator

LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):

    class Config:
        orm_mode = True


class CreateProduct(TunedModel):
    name: str
    link: str
    ave_price: float | None


class ShowProduct(TunedModel):
    id: int
    name: str
    link: str
    ave_price: float | None

