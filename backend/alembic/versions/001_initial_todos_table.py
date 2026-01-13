"""Initial todos table

Revision ID: 001
Revises:
Create Date: 2026-01-06 10:00:00.000000

"""
from typing import Sequence, Union
from datetime import datetime
import uuid

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the todos table
    op.create_table(
        'todos',
        sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('completed', sa.Boolean(), nullable=False, default=False),
        sa.Column('priority', sa.Enum('low', 'medium', 'high', name='priority'), nullable=False, default='medium'),
        sa.Column('category', sa.String(), nullable=True),
        sa.Column('due_date', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, default=datetime.utcnow),
        sa.Column('updated_at', sa.DateTime(), nullable=False, default=datetime.utcnow),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    # Drop the todos table
    op.drop_table('todos')
    # Drop the enum type
    op.execute("DROP TYPE IF EXISTS priority;")