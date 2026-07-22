from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from database.base import Base


class Order(Base):
    __tablename__ = "fact_orders"

    order_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    customer_id: Mapped[int] = mapped_column(
        ForeignKey("dim_customers.customer_id")
    )

    produit_id: Mapped[int] = mapped_column(
        ForeignKey("dim_produits.product_id")
    )

    payment_id: Mapped[int] = mapped_column(
        ForeignKey("dim_payments.payment_id")
    )

    date_id: Mapped[int] = mapped_column(
        ForeignKey("dim_date.date_id")
    )

    quantity: Mapped[int] = mapped_column(Integer)

    total_amount: Mapped[float] = mapped_column(Float)