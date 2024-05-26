"""empty message

Revision ID: 9ebbf5748e4b
Revises: c0e931e2451e
Create Date: 2024-05-26 23:25:03.670655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ebbf5748e4b'
down_revision = 'c0e931e2451e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_image_tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_image_id', sa.String(), nullable=True),
    sa.Column('tag_name', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_image_id'], ['user_images.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_image_tags')
    # ### end Alembic commands ###