from flask import Blueprint

from .. import models, schemas


breeds = Blueprint("breeds", __name__)
schema = schemas.BreedSchema()


@breeds.route("/")
def breed_list():
    breeds = models.Breed.query.all()
    return schema.dumps(breeds, many=True)


@breeds.route("/<id>")
def breed_detail(id):
    breed = models.Breed.query.get(id)
    return schema.dumps(breed)