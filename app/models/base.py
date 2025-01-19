import typing

import sqlalchemy as sa
import sqlalchemy_utils as sau
from sqlalchemy.dialects import postgresql

meta = sa.MetaData(schema='bewise')
now_at_utc = sa.text("(now() at time zone 'utc')")
generate_uuid = sa.text('uuid_generate_v4()')

common_fields = ['id', 'created', 'updated', 'archived']


def generate_base_fields() -> typing.Tuple[sa.Column, ...]:
    return (
        sa.Column('id', postgresql.UUID, unique=True, index=True, server_default=generate_uuid, nullable=False),
        sa.Column('created_at', sau.ArrowType, server_default=now_at_utc, nullable=False),
    )
