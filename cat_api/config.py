class Config:
    TESTING = False
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///../dev.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
