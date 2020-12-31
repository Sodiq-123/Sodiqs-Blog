"""empty message

Revision ID: 3adf37201b4f
Revises: 8c58c398efe1
Create Date: 2020-12-30 15:10:37.646041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3adf37201b4f'
down_revision = '8c58c398efe1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    # ### end Alembic commands ###
