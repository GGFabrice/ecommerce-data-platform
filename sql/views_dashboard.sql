-- ==========================================
-- Vue Dashboard des ventes
-- ==========================================

CREATE OR REPLACE VIEW vw_sales_dashboard AS
SELECT
    f.order_id,
    d.full_date AS order_date,
    f.quantity,
    f.total_amount,
    c.customer_id,
    p.produit_name,
    p.category
FROM fact_orders f
JOIN dim_date d
    ON f.date_id = d.date_id
JOIN dim_customers c
    ON f.customer_id = c.customer_id
JOIN dim_produits p
    ON f.produit_id = p.produit_id;


-- ==========================================
-- Vue KPI Globaux
-- ==========================================

CREATE OR REPLACE VIEW vw_kpi_global AS
SELECT
    SUM(total_amount) AS chiffre_affaires_total,
    COUNT(order_id) AS nombre_commandes,
    SUM(quantity) AS quantite_totale_vendue,
    ROUND(AVG(total_amount)::numeric,2) AS panier_moyen
FROM fact_orders;