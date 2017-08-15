"""empty message

Revision ID: b209da911e3f
Revises: c06ceda46df4
Create Date: 2017-08-10 15:49:20.831093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b209da911e3f'
down_revision = 'c06ceda46df4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('net_worth_leaderboard', sa.Column('username', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('net_worth_leaderboard', 'username')
    # ### end Alembic commands ###
