"""empty message

Revision ID: 2077e5799fa0
Revises: b209da911e3f
Create Date: 2017-08-14 22:20:22.553420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2077e5799fa0'
down_revision = 'b209da911e3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stocks', sa.Column('owner_user', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stocks', 'owner_user')
    # ### end Alembic commands ###
