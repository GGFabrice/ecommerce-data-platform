from sqlalchemy import Column, Integer, String, Float
from database.base import Base


class Produit(Base):

    __tablename__ = "dim_produits"

    produit_id = Column(
        Integer,
        primary_key=True
    )

    produit_name = Column(String(100))

    category = Column(String(100))

    prix = Column(Float)