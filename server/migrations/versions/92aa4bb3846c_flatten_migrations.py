"""Flatten migrations

Revision ID: 9a220b2c1ca7
Revises:
Create Date: 2022-11-27 20:38:54.241283

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9a220b2c1ca7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "blocklist",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("jti", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("jti"),
    )
    op.create_table(
        "settings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("smtp_host", sa.String(length=256), nullable=True),
        sa.Column("smtp_port", sa.Integer(), nullable=True),
        sa.Column("starttls", sa.Boolean(), nullable=True),
        sa.Column("ssl_tls", sa.Boolean(), nullable=True),
        sa.Column("mail_from", sa.String(length=256), nullable=True),
        sa.Column("smtp_user", sa.String(length=128), nullable=True),
        sa.Column("smtp_pass", sa.String(length=128), nullable=True),
        sa.Column("smtp_status", sa.Boolean(), nullable=True),
        sa.Column("mail_to", sa.Text(), nullable=True),
        sa.Column("webhook_url", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=128), nullable=False),
        sa.Column("password_hash", sa.Text(), nullable=False),
        sa.Column("first_login", sa.Boolean(), nullable=False),
        sa.Column("is_admin", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "client",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uid", sa.String(length=6), nullable=False),
        sa.Column("name", sa.String(length=32), nullable=False),
        sa.Column("description", sa.String(length=128), nullable=True),
        sa.Column("mail_to", sa.String(length=256), nullable=True),
        sa.Column("webhook_url", sa.Text(), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        sa.UniqueConstraint("uid"),
    )
    op.create_table(
        "xss",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("headers", sa.Text(), nullable=True),
        sa.Column("ip_addr", sa.String(length=15), nullable=True),
        sa.Column("data", sa.Text(), nullable=True),
        sa.Column("tags", sa.Text(), server_default="[]", nullable=False),
        sa.Column("timestamp", sa.Integer(), nullable=True),
        sa.Column("client_id", sa.Integer(), nullable=True),
        sa.Column("xss_type", sa.String(length=9), nullable=True),
        sa.ForeignKeyConstraint(
            ["client_id"],
            ["client.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("xss")
    op.drop_table("client")
    op.drop_table("user")
    op.drop_table("settings")
    op.drop_table("blocklist")
    # ### end Alembic commands ###
