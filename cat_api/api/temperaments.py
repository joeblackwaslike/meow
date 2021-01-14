from flask import Blueprint

from .. import models, schemas


temperaments = Blueprint("temperaments", __name__)
schema = schemas.TemperamentSchema()


@temperaments.route("/")
def temperament_list():
    temperaments = models.Temperament.query.all()
    return schema.dumps(temperaments, many=True)


@temperaments.route("/<id>")
def temperament_detail(id):
    temperament = models.Temperament.query.get(id)
    return schema.dumps(temperament)