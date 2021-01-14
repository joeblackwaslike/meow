import pytest

from cat_api.app import create_app


class TestConfig:
    TESTING = True
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@pytest.fixture(scope="session")
def app():
    test_app = create_app(config=TestConfig)

    with test_app.app_context():
        yield test_app


@pytest.fixture(scope="session")
def db(app):
    test_db = app.extensions["sqlalchemy"].db
    test_db.create_all()
    return test_db
