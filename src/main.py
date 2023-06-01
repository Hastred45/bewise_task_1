from fastapi import FastAPI

from src.questions.routers import router


app = FastAPI(
    title='Bewise.Quiz',
    description='Сервис генерации вопросов для викторин'
)

app.include_router(router)
