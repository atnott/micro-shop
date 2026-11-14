"""create users table

Revision ID: 53e0d861f2e4
Revises:
Create Date: 2026-11-15 00:56:14.684978

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "53e0d861f2e4"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("name", name=op.f("uq_users_name")),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
