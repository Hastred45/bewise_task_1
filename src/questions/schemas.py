from typing import Optional

from pydantic import BaseModel


class LastQuestion(BaseModel):
    question: Optional[str]
    answer: Optional[str]

    class Config:
        orm_mode = True


class QuestionQuantity(BaseModel):
    quantity: Optional[int]

    class Config:
        orm_mode = True
