from .db import cli as db_cli


def setup(app):
    app.cli.add_command(db_cli)