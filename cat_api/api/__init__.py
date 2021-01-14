from .breeds import breeds
from .temperaments import temperaments


def register(app):
    app.register_blueprint(breeds, url_prefix="/breeds")
    app.register_blueprint(temperaments, url_prefix="/temperaments")
