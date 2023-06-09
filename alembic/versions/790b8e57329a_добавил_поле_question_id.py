"""добавил поле question_id

Revision ID: 790b8e57329a
Revises: 47f960054684
Create Date: 2023-05-17 15:01:19.834374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '790b8e57329a'
down_revision = '47f960054684'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('question_id', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('question', 'question_id')
    # ### end Alembic commands ###
