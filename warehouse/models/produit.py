from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Produit(Base):
    __tablename__ = "dim_produits"

    produit_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    produit_name: Mapped[str] = mapped_column(String(100))
    category: Mapped[str] = mapped_column(String(100))
    unit_prix: Mapped[float] = mapped_column(Float)