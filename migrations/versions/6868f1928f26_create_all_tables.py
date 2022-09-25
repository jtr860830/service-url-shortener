"""create all tables

Revision ID: 6868f1928f26
Revises: Josh
Create Date: 2022-09-25 01:20:01.725645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6868f1928f26"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, nullable=False, primary_key=True),
        sa.Column("username", sa.String, nullable=False, unique=True, index=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column(
            "create_time",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )

    op.create_table(
        "urls",
        sa.Column(
            "user_id",
            sa.Integer,
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("alias", sa.String, nullable=False, primary_key=True),
        sa.Column("original", sa.String, nullable=False),
        sa.Column(
            "create_time",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("now()"),
        ),
    )


def downgrade() -> None:
    op.drop_table("urls")
    op.drop_table("users")
