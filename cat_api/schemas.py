from flask_marshmallow import Marshmallow

from . import models


ma = Marshmallow()


def setup(app):
    ma.init_app(app)


class BreedSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Breed

    temperaments = ma.List(ma.HyperlinkRelated("temperaments.temperament_detail"))


class TemperamentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = models.Temperament

    breeds = ma.List(ma.HyperlinkRelated("breeds.breed_detail"))
