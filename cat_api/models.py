from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Temperament(Base):
    __tablename__ = "temperaments"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    breeds = relationship(
        "Breed", secondary="breeds_temperaments", back_populates="temperaments"
    )


class Breed(Base):
    __tablename__ = "breeds"
    id = Column(Integer, primary_key=True)

    name = Column(String(255), nullable=False)
    origin = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)

    temperaments = relationship(
        "Temperament", secondary="breeds_temperaments", back_populates="breeds"
    )


breeds_temperaments = Table(
    "breeds_temperaments",
    Base.metadata,
    Column("breed_id", ForeignKey("breeds.id"), primary_key=True),
    Column("temperament_id", ForeignKey("temperaments.id"), primary_key=True),
)
