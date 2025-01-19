import sqlalchemy as sa

from .base import generate_base_fields, meta

applications = sa.Table(
    'applications',
    meta,
    *generate_base_fields(),
    sa.Column('user_name', sa.String(100), nullable=False),
    sa.Column('description', sa.String(300), nullable=False),  # Noqa: WPS432
)
