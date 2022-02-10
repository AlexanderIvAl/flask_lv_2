"""add role

Revision ID: e370710a0c92
Revises: 333ea2deaeb9
Create Date: 2022-02-10 13:02:30.345684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e370710a0c92'
down_revision = '333ea2deaeb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_model', sa.Column('role', sa.String(length=32), server_default='simple_user', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_model', 'role')
    # ### end Alembic commands ###
