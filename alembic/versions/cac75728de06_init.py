"""init

Revision ID: cac75728de06
Revises: 
Create Date: 2022-02-20 19:00:59.015969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cac75728de06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Account',
        sa.Column('account_no', sa.Integer, primary_key= True),
        sa.Column('date', sa.String, nullable= False),
        sa.Column('transaction_details'), sa.String, nullable= False),
        sa.Column('value_date', sa.String, nullable= False),
        sa.Column('withdrawl_amt', sa.String, nullable= False),
        sa.Column('deposit_amt', sa.String, nullable= False),
        sa.Column('balance_amt', sa.String, nullable= False)
    )


def downgrade():
    op.drop_table('Account')
