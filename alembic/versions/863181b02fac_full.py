"""full

Revision ID: 863181b02fac
Revises: 2d82bbaa3c77

"""
import sqlalchemy as sa

from alembic import op


# revision identifiers, used by Alembic.
revision = '863181b02fac'
down_revision = '7f35799379c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'status',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )
    op.create_table(
        'vacancies',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String()),
        sa.UniqueConstraint('name'),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'profiles',
        sa.Column('id', sa.Integer()),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('status_id', sa.Integer()),
        sa.UniqueConstraint('email'),
        sa.ForeignKeyConstraint(
            ['status_id'],
            ['status.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'profile_vacancy',
        sa.Column('profile_id', sa.Integer(), nullable=False),
        sa.Column('vacancy_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['profile_id'],
            ['profiles.id'],
        ),
        sa.ForeignKeyConstraint(
            ['vacancy_id'],
            ['vacancies.id'],
        ),
        sa.PrimaryKeyConstraint('profile_id', 'vacancy_id'),
    )
    op.create_unique_constraint(
        'uix_profile_vacancy_id', 'profile_vacancy', ['profile_id', 'vacancy_id']
    )


def downgrade() -> None:
    op.drop_constraint('uix_profile_vacancy_id', 'profile_vacancy', type_='unique')
    op.drop_table('profile_vacancy')
    op.drop_table('profiles')
    op.drop_table('vacancies')
    op.drop_table('status')
