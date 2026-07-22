from database.base import Base
from database.connection import engine

# Import des modèles
from warehouse.models.customer import Customer
from warehouse.models.produit import Produit
from warehouse.models.date import Date
from warehouse.models.payment import Payment
from warehouse.models.order import Order

Base.metadata.create_all(engine)

print("✅ Toutes les tables ont été créées avec succès.")