from cat_api import models


def test_breeds(db):
    b = models.Breed(name="cutie", description="sdfsfsdf", origin="Germany")
    db.session.add(b)
    db.session.commit()

    assert b.id and b.name


def test_temperaments(db):
    t = models.Temperament(name="cutie")
    db.session.add(t)
    db.session.commit()

    assert t.id


def test_breeds_with_temperaments(db):
    b = models.Breed(
        name="Scottish Fold", description="fluffy", origin="Scotland"
    )
    t = models.Temperament(name="joe")
    b.temperaments.append(t)

    db.session.add(b)
    db.session.commit()

    assert t in b.temperaments
