"""Initial migration for Employ table

Revision ID: 4570000ca794
Revises: 
Create Date: 2024-12-21 22:00:39.612367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4570000ca794'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employ',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('department', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employ')
    # ### end Alembic commands ###