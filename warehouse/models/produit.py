from sqlalchemy import Column, Integer, String, Float
from database.base import Base


class Produit(Base):

    __tablename__ = "dim_produits"

    product_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    product_name = Column(String)
    category = Column(String)
    price = Column(Float)