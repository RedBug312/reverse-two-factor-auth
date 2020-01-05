"""empty message

Revision ID: cf57d6811c7a
Revises: 
Create Date: 2020-01-05 00:28:36.679005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf57d6811c7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('badges', sa.String(length=64), nullable=True))
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=32),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=32),
               nullable=True)
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
        batch_op.drop_column('badges')

    # ### end Alembic commands ###
