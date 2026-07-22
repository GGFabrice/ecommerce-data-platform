from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Payment(Base):
    __tablename__ = "dim_payments"

    payment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    payment_method: Mapped[str] = mapped_column(String(50))