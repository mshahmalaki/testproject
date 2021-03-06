"""empty message

Revision ID: 248215860020
Revises: e640a82a241e
Create Date: 2020-07-26 15:40:30.165726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '248215860020'
down_revision = 'e640a82a241e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('address', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'address')
    # ### end Alembic commands ###
