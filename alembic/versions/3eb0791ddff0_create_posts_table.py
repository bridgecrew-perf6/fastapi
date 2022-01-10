"""create posts table

Revision ID: 3eb0791ddff0
Revises: 
Create Date: 2022-01-09 04:34:28.274780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3eb0791ddff0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table("posts")
