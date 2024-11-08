"""empty message

Revision ID: 16111d5bcc29
Revises: a5cffa318ac2
Create Date: 2024-11-04 21:25:45.294172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16111d5bcc29'
down_revision = 'a5cffa318ac2'
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
    sa.UniqueConstraint('id_people'),
    sa.UniqueConstraint('id_planet'),
    sa.UniqueConstraint('id_starship')
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
    sa.UniqueConstraint('age'),
    sa.UniqueConstraint('force_side'),
    sa.UniqueConstraint('parents'),
    sa.UniqueConstraint('teacher'),
    sa.UniqueConstraint('type_warrior')
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
    sa.Column('description_starship', sa.Boolean(), nullable=False),
    sa.Column('model', sa.String(length=50), nullable=False),
    sa.Column('cargo_capacity', sa.Integer(), nullable=False),
    sa.Column('speed', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description_starship'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url_starship')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=200),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    op.drop_table('starship')
    op.drop_table('planet')
    op.drop_table('people')
    op.drop_table('character')
    # ### end Alembic commands ###