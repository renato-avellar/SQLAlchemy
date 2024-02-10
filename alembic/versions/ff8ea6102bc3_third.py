"""third

Revision ID: ff8ea6102bc3
Revises: 335d02ca7a57
Create Date: 2024-02-10 02:13:27.322300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff8ea6102bc3'
down_revision: Union[str, None] = '335d02ca7a57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL("INSERT INTO filmes (titulo, genero, ano) VALUES ('Estou', 'aqui', 777);"))


def downgrade() -> None:
    op.execute(sa.DDL("DELETE FROM filmes WHERE titulo = 'Estou';"))