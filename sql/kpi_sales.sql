-- ==========================================
-- KPI SALES - ANALYSE DES VENTES
-- Data Warehouse Ecommerce
-- ==========================================


-- 1. Chiffre d'affaires total

SELECT 
    SUM(total_amount) AS chiffre_affaires_total
FROM fact_orders;


-- 2. Nombre total de commandes

SELECT
    COUNT(order_id) AS nombre_commandes
FROM fact_orders;


-- 3. Quantité totale vendue

SELECT
    SUM(quantity) AS quantite_totale_vendue
FROM fact_orders;


-- 4. Panier moyen

SELECT
    ROUND(AVG(total_amount)::numeric,2) AS panier_moyen
FROM fact_orders;