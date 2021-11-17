"""create posts table

Revision ID: b31a0c41c139
Revises: 
Create Date: 2021-11-16 18:39:41.223420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b31a0c41c139"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
