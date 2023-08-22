"""first commit

Revision ID: 10f6f2edfd70
Revises: 
Create Date: 2023-08-21 06:34:07.934641

"""
from typing import Sequence, Union

import fastapi_users_db_sqlalchemy
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '10f6f2edfd70'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('user',
                    sa.Column('id', fastapi_users_db_sqlalchemy.generics.GUID(), nullable=False),
                    sa.Column('email', sa.String(length=320), unique=True, nullable=False),
                    sa.Column('first_name', sa.String(length=100), nullable=False),
                    sa.Column('last_name', sa.String(length=100), nullable=False),
                    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.Column('birthdate', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
