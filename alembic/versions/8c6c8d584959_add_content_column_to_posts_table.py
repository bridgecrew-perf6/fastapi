"""add content column to posts table

Revision ID: 8c6c8d584959
Revises: 3eb0791ddff0
Create Date: 2022-01-09 12:05:07.043639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8c6c8d584959"
down_revision = "3eb0791ddff0"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")
