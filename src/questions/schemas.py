from typing import Optional

from pydantic import BaseModel


class Questions(BaseModel):
    question: Optional[str]
    answer: Optional[str]

    class Config:
        orm_mode = True


class QuestionQuantity(BaseModel):
    quantity: int

    class Config:
        orm_mode = True
