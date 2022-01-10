"""add foreign key to posts table

Revision ID: 992182bd06c2
Revises: a5a5b1d4bd54
Create Date: 2022-01-10 08:40:03.339739

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "992182bd06c2"
down_revision = "a5a5b1d4bd54"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
