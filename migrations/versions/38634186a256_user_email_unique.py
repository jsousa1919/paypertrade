"""user email unique

Revision ID: 38634186a256
Revises: 5a5b5b13534d
Create Date: 2014-08-20 02:47:07.334432

"""

# revision identifiers, used by Alembic.
revision = '38634186a256'
down_revision = '5a5b5b13534d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'user', ['email'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user')
    ### end Alembic commands ###
