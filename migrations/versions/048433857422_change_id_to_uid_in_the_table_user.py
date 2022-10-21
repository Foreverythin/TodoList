"""change id to uid in the table User

Revision ID: 048433857422
Revises: fed9a7af45f8
Create Date: 2022-10-22 00:29:03.276383

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '048433857422'
down_revision = 'fed9a7af45f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('uid', sa.Integer(), autoincrement=True, nullable=False))
    op.drop_column('user', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('user', 'uid')
    # ### end Alembic commands ###
