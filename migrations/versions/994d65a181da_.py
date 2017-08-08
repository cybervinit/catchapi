"""empty message

Revision ID: 994d65a181da
Revises: 435963f4aebe
Create Date: 2017-08-08 15:23:29.853162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '994d65a181da'
down_revision = '435963f4aebe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leaderboard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_table('leaderboard')
    # ### end Alembic commands ###
