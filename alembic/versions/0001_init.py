"""Create bewise schema.

Revision ID: 0001
Revises:
Create Date: 2025-01-20 10:24:41.446111

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    op.execute('CREATE SCHEMA IF NOT EXISTS bewise;')


def downgrade() -> None:
    op.execute('DROP SCHEMA bewise CASCADE;')
