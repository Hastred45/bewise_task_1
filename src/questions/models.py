from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.models import Base


class Question(Base):
    __tablename__ = 'question'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    question_id: Mapped[int] = mapped_column(nullable=False)
    question: Mapped[str] = mapped_column(nullable=False)
    answer: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False)
    inserted_at: Mapped[datetime] = mapped_column(default=func.now())
