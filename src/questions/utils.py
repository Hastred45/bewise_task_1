import httpx
from fastapi import HTTPException


async def get_response(questions_num: int) -> dict:
    '''Асинхронный запрос к сервису вопросов для викторин'''
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f'https://jservice.io/api/random?count={questions_num}'
            )
        return response.json()
    except httpx.HTTPError:
        raise HTTPException(status_code=503,
                            detail='ConnectionError')
