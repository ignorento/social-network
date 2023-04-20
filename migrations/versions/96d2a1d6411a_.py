"""empty message

Revision ID: 96d2a1d6411a
Revises: 30411769e319
Create Date: 2023-04-11 23:25:54.584997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96d2a1d6411a'
down_revision = '30411769e319'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follows',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followee_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['followee_id'], ['user.id'], name='fk_follows_followee_id'),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], name='fk_follows_follower_id'),
    sa.PrimaryKeyConstraint('follower_id', 'followee_id')
    )
    op.create_table('posts',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], name='fk_posts_author_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dislikes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='fk_dislikes_post_id'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_dislikes_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('likes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='fk_likes_post_id'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_likes_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))
        batch_op.drop_index('idx-profiles_user_id')
        batch_op.create_index('idx_profiles_user_id', ['user_id'], unique=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.drop_index('idx_profiles_user_id')
        batch_op.create_index('idx-profiles_user_id', ['user_id'], unique=False)
        batch_op.drop_column('last_seen')

    op.drop_table('likes')
    op.drop_table('dislikes')
    op.drop_table('posts')
    op.drop_table('follows')
    # ### end Alembic commands ###
