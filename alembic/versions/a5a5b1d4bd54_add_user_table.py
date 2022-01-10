"""add user table

Revision ID: a5a5b1d4bd54
Revises: 8c6c8d584959
Create Date: 2022-01-09 12:12:21.726284

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.sqltypes import String


# revision identifiers, used by Alembic.
revision = "a5a5b1d4bd54"
down_revision = "8c6c8d584959"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade():
    op.drop_table("users")
