"""empty message

Revision ID: ce77b4d6b9f9
Revises: 91a5578ce728
Create Date: 2023-04-14 16:17:07.467361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce77b4d6b9f9'
down_revision = '91a5578ce728'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('follows', schema=None) as batch_op:
        batch_op.add_column(sa.Column('following_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('fk_follows_followee_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_follows_following_id', 'user', ['following_id'], ['id'])
        batch_op.drop_column('followee_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('follows', schema=None) as batch_op:
        batch_op.add_column(sa.Column('followee_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint('fk_follows_following_id', type_='foreignkey')
        batch_op.create_foreign_key('fk_follows_followee_id', 'user', ['followee_id'], ['id'])
        batch_op.drop_column('following_id')

    # ### end Alembic commands ###
