"""empty message

Revision ID: 3e68deca1c5d
Revises: ddd98d22cba2
Create Date: 2023-04-01 23:26:31.860737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e68deca1c5d'
down_revision = 'ddd98d22cba2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=True))
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_email'))
        batch_op.drop_column('email')

    # ### end Alembic commands ###
