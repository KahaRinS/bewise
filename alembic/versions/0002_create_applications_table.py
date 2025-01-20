"""create applications table

Revision ID: 0002
Revises: 0001
Create Date: 2025-01-17 15:00:46.552664

"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '0002'
down_revision: Union[str, None] = '0001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'applications',
        sa.Column(
            'id',
            postgresql.UUID(),
            server_default=sa.text('uuid_generate_v4()'),
            nullable=False,
        ),
        sa.Column(
            'created_at',
            sqlalchemy_utils.types.arrow.ArrowType(),
            server_default=sa.text("(now() at time zone 'utc')"),
            nullable=False,
        ),
        sa.Column('user_name', sa.String(length=100), nullable=False),
        sa.Column('description', sa.String(length=300), nullable=False),
        schema='bewise'
    )
    op.create_index(
        op.f('ix_bewise_applications_id'),
        'applications', ['id'], unique=True, schema='bewise')


def downgrade() -> None:
    op.drop_index(op.f('ix_bewise_applications_id'), table_name='applications', schema='bewise')
    op.drop_table('applications', schema='bewise')
