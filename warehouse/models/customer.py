from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Customer(Base):
    __tablename__ = "dim_customers"

    customer_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    city: Mapped[str] = mapped_column(String(100))
    country: Mapped[str] = mapped_column(String(100))