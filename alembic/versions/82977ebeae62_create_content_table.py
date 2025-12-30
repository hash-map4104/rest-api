"""create content table

Revision ID: 82977ebeae62
Revises: 
Create Date: 2025-12-30 16:24:50.026375

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82977ebeae62'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('content',
                    sa.Column ('id',
                               sa.Integer(),
                               nullable=False,
                               primary_key=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('content')
    pass
