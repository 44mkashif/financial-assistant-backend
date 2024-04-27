"""seed dummy user data

Revision ID: 486a7666bce6
Revises: 0827ca2ab2fb
Create Date: 2024-04-27 13:43:57.514655

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.sql import table, column
from sqlalchemy.dialects import postgresql
from werkzeug.security import generate_password_hash

# revision identifiers, used by Alembic.
revision = '486a7666bce6'
down_revision = '0827ca2ab2fb'
branch_labels = None
depends_on = None


def upgrade():
    user_table = table('User',
        column('id', sa.Integer),
        column('name', sa.String),
        column('email', sa.String),
        column('password', sa.String),
        column('created_at', sa.DateTime),
        column('updated_at', sa.DateTime)
    )

    op.bulk_insert(user_table,
        [
            {'name': 'Muhammad Kashif', 'email': '44mkashif@gmail.com', 'password': generate_password_hash('password'), 'created_at': datetime.now(), 'updated_at': datetime.now()},
            {'name': 'Tax GPT', 'email': 'taxgpt@yopmail.com', 'password': generate_password_hash('password'), 'created_at': datetime.now(), 'updated_at': datetime.now()}
        ]
    )


def downgrade():
    pass
