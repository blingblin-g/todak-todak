"""empty message

Revision ID: 98cff732c35b
Revises: 7158daee6622
Create Date: 2021-04-02 08:34:07.203115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98cff732c35b'
down_revision = '7158daee6622'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nickname', sa.String(length=32), nullable=True),
    sa.Column('email', sa.String(length=32), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('pw', sa.String(length=100), nullable=False),
    sa.Column('data', sa.DATE(), nullable=True),
    sa.Column('usertype', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nickname'),
    mysql_collate='utf8_general_ci'
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
