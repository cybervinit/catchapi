"""empty message

Revision ID: c06ceda46df4
Revises: 994d65a181da
Create Date: 2017-08-08 15:32:34.717999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c06ceda46df4'
down_revision = '994d65a181da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('net_worth_leaderboard',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('leaderboard')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leaderboard',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('rank', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], [u'users.id'], name=u'leaderboard_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'leaderboard_pkey')
    )
    op.drop_table('net_worth_leaderboard')
    # ### end Alembic commands ###