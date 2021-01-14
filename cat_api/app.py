from flask import Flask
from flask_cors import CORS

from . import database, schemas, api, commands


def create_app(config="cat_api.config.Config"):
    app = Flask(__name__)
    app.config.from_object(config)

    database.setup(app)
    schemas.setup(app)
    api.register(app)
    commands.setup(app)

    CORS(app)

    return app
