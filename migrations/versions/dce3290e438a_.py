"""empty message

Revision ID: dce3290e438a
Revises: 
Create Date: 2025-01-14 15:18:04.266500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dce3290e438a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Animals',
    sa.Column('nick_name', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('ALIVE', 'SOLD', 'UNKNOW', name='animalstatusenum'), nullable=False),
    sa.Column('weight', sa.DECIMAL(precision=6, scale=2), nullable=False),
    sa.Column('sex', sa.Enum('MALE', 'FEMALE', name='animalsexenum'), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Animals')
    # ### end Alembic commands ###
