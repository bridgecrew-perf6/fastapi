"""add last few columns to post table

Revision ID: 11cbac17ad77
Revises: 992182bd06c2
Create Date: 2022-01-10 08:49:32.525311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "11cbac17ad77"
down_revision = "992182bd06c2"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )


def downgrade():
    op.drop_column("posts", column_name="published")
    op.drop_column("posts", column_name="created_at")
