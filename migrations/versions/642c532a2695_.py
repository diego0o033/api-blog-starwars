"""empty message

Revision ID: 642c532a2695
Revises: 
Create Date: 2024-11-11 21:21:31.357838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '642c532a2695'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_people', sa.Integer(), nullable=False),
    sa.Column('id_planet', sa.Integer(), nullable=False),
    sa.Column('id_starship', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_people')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('url_img_people', sa.String(length=200), nullable=False),
    sa.Column('description_people', sa.String(length=1000), nullable=False),
    sa.Column('film_people', sa.String(length=500), nullable=False),
    sa.Column('url_img_starship_people', sa.String(length=200), nullable=False),
    sa.Column('force_side', sa.String(length=20), nullable=False),
    sa.Column('type_warrior', sa.Integer(), nullable=False),
    sa.Column('parents', sa.Boolean(), nullable=False),
    sa.Column('teacher', sa.Boolean(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('age')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('url_planet', sa.String(length=200), nullable=False),
    sa.Column('description_planet', sa.String(length=1000), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('starship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=False),
    sa.Column('url_starship', sa.Integer(), nullable=False),
    sa.Column('description_starship', sa.String(length=1000), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('cargo_capacity', sa.Integer(), nullable=False),
    sa.Column('speed', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('starship')
    op.drop_table('planet')
    op.drop_table('people')
    op.drop_table('character')
    # ### end Alembic commands ###
