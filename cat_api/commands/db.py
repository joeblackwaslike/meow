from flask.cli import AppGroup

from ..database import db, models
from ..tcaclient import TCAClient


cli = AppGroup("db")


@cli.command("init")
def init_db():
    db.create_all()


@cli.command("clear")
def clear_db():
    db.drop_all()
    db.create_all()


@cli.command("load-breeds")
def load_breeds():
    client = TCAClient()
    breeds = client.get_breeds()

    temperaments = {}

    def create_or_get(name):
        if name not in temperaments:
            temperaments[name] = models.Temperament(name=name)
        return temperaments[name]

    for breed in breeds:
        b = models.Breed(
            name=breed["name"],
            origin=breed["origin"],
            description=breed["description"],
        )
        for t in breed["temperament"].split(", "):
            b.temperaments.append(create_or_get(t))

        db.session.add(b)

    db.session.commit()
