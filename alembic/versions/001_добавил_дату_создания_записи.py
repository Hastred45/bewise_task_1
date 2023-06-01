"""Добавление столбца inserted_at в таблицу question

Revision ID: 001
Revises: 790b8e57329a
Create Date: 2023-05-17 14:14:18.427219
"""

from alembic import op
import sqlalchemy as sa


# Определение версии миграции
revision = '001'
down_revision = '790b8e57329a'
branch_labels = None
depends_on = None


def upgrade():
    # Создание столбца inserted_at с использованием функции func.now()
    op.add_column('question', sa.Column('inserted_at', sa.DateTime(), server_default=sa.func.now(), nullable=True))


def downgrade():
    # Удаление столбца inserted_at
    op.drop_column('question', 'inserted_at')
