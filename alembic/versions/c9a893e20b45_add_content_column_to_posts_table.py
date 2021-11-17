"""add content column to posts table

Revision ID: c9a893e20b45
Revises: b31a0c41c139
Create Date: 2021-11-16 18:58:54.609363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c9a893e20b45"
down_revision = "b31a0c41c139"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
