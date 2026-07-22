from extract import extract_data


customers, produits, orders = extract_data()

print(customers.head())

print(produits.head())

print(orders.head())