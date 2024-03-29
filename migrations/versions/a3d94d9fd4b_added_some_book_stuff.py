"""added some book stuff

Revision ID: a3d94d9fd4b
Revises: 404ee8a4a2b8
Create Date: 2014-07-17 23:40:46.665317

"""

# revision identifiers, used by Alembic.
revision = 'a3d94d9fd4b'
down_revision = '404ee8a4a2b8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('isbn', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book_tag_map',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'tag_id')
    )
    op.create_table('book_author_map',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'author_id')
    )
    op.add_column(u'user', sa.Column('token', sa.String(length=64), nullable=True))
    op.drop_column(u'user', 'username')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('user_username_key', 'user', ['username'], unique=True)
    op.create_unique_constraint(u'user_username_key', 'user', ['username'])
    op.add_column(u'user', sa.Column('username', sa.VARCHAR(length=32), autoincrement=False, nullable=False))
    op.drop_column(u'user', 'token')
    op.drop_table('book_author_map')
    op.drop_table('book_tag_map')
    op.drop_table('tag')
    op.drop_table('book')
    op.drop_table('author')
    ### end Alembic commands ###
