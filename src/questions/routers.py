from typing import Annotated, Dict, List, Union

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils import check_db
from src.questions.crud import (add_question,
                                get_questions_from_database,
                                quantity)
from src.questions.schemas import LastQuestion, QuestionQuantity
from src.questions.utils import get_response

router = APIRouter(prefix='/question', tags=['questions'])


@router.post('/',
             summary='Запрос вопросов',
             response_model=Union[List[LastQuestion], LastQuestion])
async def request_question(
    quest_num: int,
    db: Annotated[AsyncSession, Depends(check_db)]
) -> List[Dict[str, str]]:
    '''
    Ваш список вопросов и ответов для викторин запрашивается
    у сервиса, сохраняется в БД и затем вы получаете его.
    '''
    response = await get_response(quest_num)
    await add_question(response, db)
    return await get_questions_from_database(quest_num, db)


@router.get('/',
            summary='Сколько вопросов есть в БД',
            response_model=QuestionQuantity)
async def get_quantity(
    db: Annotated[AsyncSession, Depends(check_db)]
) -> Dict[str, str]:
    '''Сколько вопросов в базе?'''
    return await quantity(db)


@router.get('/{num}',
            summary='Получить вопросы из БД',
            response_model=Union[List[LastQuestion], LastQuestion])
async def get_quest(
    num: int,
    db: Annotated[AsyncSession, Depends(check_db)]
) -> List[Dict[str, str]]:
    '''Если в базе уже есть вопросы'''
    return await get_questions_from_database(num, db)
