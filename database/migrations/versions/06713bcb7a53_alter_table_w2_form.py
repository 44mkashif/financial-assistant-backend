"""alter table w2 form

Revision ID: 06713bcb7a53
Revises: 0827ca2ab2fb
Create Date: 2024-04-28 21:49:55.088455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06713bcb7a53'
down_revision = '0827ca2ab2fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('W2Form', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gpt_assistant_id', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('gpt_thread_id', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('W2Form', schema=None) as batch_op:
        batch_op.drop_column('gpt_thread_id')
        batch_op.drop_column('gpt_assistant_id')

    # ### end Alembic commands ###
