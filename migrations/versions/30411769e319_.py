"""empty message

Revision ID: 30411769e319
Revises: b3dd06be1abe
Create Date: 2023-04-07 12:26:10.547374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30411769e319'
down_revision = 'b3dd06be1abe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('facebook', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.drop_column('facebook')

    # ### end Alembic commands ###
