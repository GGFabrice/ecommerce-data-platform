from sqlalchemy import Integer, Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from database.base import Base


class Date(Base):
    __tablename__ = "dim_date"

    date_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    full_date: Mapped[date] = mapped_column(Date, unique=True)

    day: Mapped[int] = mapped_column(Integer)

    month: Mapped[int] = mapped_column(Integer)

    year: Mapped[int] = mapped_column(Integer)