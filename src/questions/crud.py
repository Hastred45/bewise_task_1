from datetime import datetime
from typing import List, Union

from fastapi import HTTPException
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.questions.models import Question
from src.questions.schemas import LastQuestion, QuestionQuantity
from src.questions.utils import get_response


async def get_questions_from_database(
        quest_num: int,
        db: AsyncSession
) -> Union[List[LastQuestion], LastQuestion]:
    query_results = await db.execute(
        select(Question).order_by(desc('inserted_at')).limit(quest_num)
    )
    query_results = query_results.scalars().all()
    if not query_results:
        return LastQuestion(question='No questions in DB')
    question_results = [
        LastQuestion(question=quest.question, answer=quest.answer)
        for quest in query_results
    ]
    return question_results


async def add_question(response: dict, db: AsyncSession) -> None:
    if response is None:
        raise HTTPException(
            status_code=404,
            detail='Question is not found'
        )
    count = 0
    for ques in response:
        question_id = ques.get('id')
        exists = await db.execute(
            select(Question).filter(Question.question_id == question_id)
        )
        if not exists.scalars().first():
            question = Question(
                question_id=ques.get('id'),
                question=ques.get('question'),
                answer=ques.get('answer'),
                created_at=datetime.strptime(
                    ques.get('created_at'), '%Y-%m-%dT%H:%M:%S.%fZ'
                )
            )
            db.add(question)
            await db.commit()
            await db.refresh(question)
        else:
            count += 1
            continue

    if count != 0:
        response = await get_response(count)
        await add_question(response, db)


async def quantity(db: AsyncSession) -> QuestionQuantity:
    query_results = await db.execute(select(Question))
    query_results = query_results.scalars().all()
    total_count = QuestionQuantity(quantity=len(query_results))
    return total_count
