"""empty message

Revision ID: 6af02023bfab
Revises: 2077e5799fa0
Create Date: 2017-08-14 22:22:24.792697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6af02023bfab'
down_revision = '2077e5799fa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stocks', 'owner_user',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stocks', 'owner_user',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###
