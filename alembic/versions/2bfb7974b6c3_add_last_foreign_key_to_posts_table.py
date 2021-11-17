"""add last foreign key to posts table

Revision ID: 2bfb7974b6c3
Revises: 7d88f3dee776
Create Date: 2021-11-16 19:15:38.894825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2bfb7974b6c3"
down_revision = "7d88f3dee776"
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
    pass


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
