from flask_sqlalchemy import SQLAlchemy

from . import models


db = SQLAlchemy(metadata=models.Base.metadata)


def setup(app):
    db.init_app(app)

    def setup_session():
        models.Base.query = db.session.query_property()
    
    app.before_first_request(setup_session)