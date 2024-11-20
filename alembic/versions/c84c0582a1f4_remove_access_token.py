"""remove_access_token

Revision ID: c84c0582a1f4
Revises: 66985f8132a2
Create Date: 2024-11-17 03:05:54.088643

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c84c0582a1f4'
down_revision: Union[str, None] = '66985f8132a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('UserProfile', 'access_token')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('UserProfile', sa.Column('access_token', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
