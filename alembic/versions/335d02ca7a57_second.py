"""second

Revision ID: 335d02ca7a57
Revises: f05c30101f3e
Create Date: 2024-02-10 02:09:48.507140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from infra.repository.filmes_repository import FilmesRepository
from infra.repository.atores_repository import Atores
from infra.configs.connection import DBConnectionHandler


# revision identifiers, used by Alembic.
revision: str = '335d02ca7a57'
down_revision: Union[str, None] = 'f05c30101f3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    filmes_repository = FilmesRepository(DBConnectionHandler)
    filmes_repository.insert('ola', 'mundo', 123)


def downgrade() -> None:
    filmes_repository = FilmesRepository(DBConnectionHandler)
    filmes_repository.delete('ola')
