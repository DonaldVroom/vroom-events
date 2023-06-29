"""empty message

Revision ID: d74ea0d2c946
Revises: cae99fdfb3bb
Create Date: 2023-06-29 12:59:02.850204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd74ea0d2c946'
down_revision = 'cae99fdfb3bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('qteamevent2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('q1', sa.String(), nullable=False),
    sa.Column('q2', sa.String(), nullable=False),
    sa.Column('q3', sa.String(), nullable=False),
    sa.Column('q4', sa.Integer(), nullable=False),
    sa.Column('how_many_people', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('locale', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('qteamevent2', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_qteamevent2_created'), ['created'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('qteamevent2', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_qteamevent2_created'))

    op.drop_table('qteamevent2')
    # ### end Alembic commands ###