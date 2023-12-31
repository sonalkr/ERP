"""Initial migration

Revision ID: a73d46007940
Revises: 
Create Date: 2023-12-21 22:43:18.656629

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a73d46007940'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('unit_name', sa.Enum('BAG', 'BDL', 'BAL', 'BKL', 'BOU', 'BOX', 'BTL', 'BUN', 'CAN', 'CTN', 'DOZ', 'DRM', 'GGR', 'GRS', 'NOS', 'PAC', 'PCS', 'PRS', 'ROL', 'SET', 'TBS', 'TGM', 'THD', 'TUB', 'UNT', 'CBM', 'CCM', 'KLR', 'MLT', 'UGS', 'SQF', 'SQM', 'SQY', 'GYD', 'KME', 'MTR', 'YDS', 'CMS', 'TON', 'QTL', 'GMS', 'KGS', 'OTH', name='unitnameenum'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_units_id'), 'units', ['id'], unique=False)
    op.create_table('inventorys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('desc', sa.String(), nullable=True),
    sa.Column('qty', sa.Float(), nullable=True),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('Freight', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['unit_id'], ['units.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventorys_id'), 'inventorys', ['id'], unique=False)
    op.create_index(op.f('ix_inventorys_name'), 'inventorys', ['name'], unique=True)
    op.create_index(op.f('ix_inventorys_sku'), 'inventorys', ['sku'], unique=True)
    op.create_table('vouchers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('dc_no', sa.String(), nullable=True),
    sa.Column('ledger_id', sa.Integer(), nullable=True),
    sa.Column('qty', sa.Float(), nullable=True),
    sa.Column('rate', sa.Float(), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('invoice_no', sa.String(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ledger_id'], ['ledgers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vouchers_id'), 'vouchers', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_vouchers_id'), table_name='vouchers')
    op.drop_table('vouchers')
    op.drop_index(op.f('ix_inventorys_sku'), table_name='inventorys')
    op.drop_index(op.f('ix_inventorys_name'), table_name='inventorys')
    op.drop_index(op.f('ix_inventorys_id'), table_name='inventorys')
    op.drop_table('inventorys')
    op.drop_index(op.f('ix_units_id'), table_name='units')
    op.drop_table('units')
    # ### end Alembic commands ###
