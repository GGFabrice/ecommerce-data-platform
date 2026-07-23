from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Payment(Base):
    __tablename__ = "dim_payments"

    payment_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    order_id: Mapped[int] = mapped_column(Integer)

    amount: Mapped[float] = mapped_column(Float)

    payment_method: Mapped[str] = mapped_column(String(50))