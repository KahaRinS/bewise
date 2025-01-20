import sqlalchemy as sa

from .base import Base


class Applications(Base):
    __tablename__ = 'applications'
    __table_args__ = {'schema': 'bewise'}

    user_name = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.String(300), nullable=True)
