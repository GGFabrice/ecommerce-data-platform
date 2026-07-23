-- ==========================================
-- KPI PRODUITS
-- ==========================================


-- 1. Top 10 produits par quantité vendue

SELECT 
    p.produit_name,
    SUM(f.quantity) AS quantite_vendue
FROM fact_orders f
JOIN dim_produits p
ON f.produit_id = p.produit_id
GROUP BY p.produit_name
ORDER BY quantite_vendue DESC
LIMIT 10;



-- 2. Top 10 produits par chiffre d'affaires

SELECT
    p.produit_name,
    SUM(f.total_amount) AS chiffre_affaires
FROM fact_orders f
JOIN dim_produits p
ON f.produit_id = p.produit_id
GROUP BY p.produit_name
ORDER BY chiffre_affaires DESC
LIMIT 10;



-- 3. Chiffre d'affaires par catégorie

SELECT
    p.category,
    SUM(f.total_amount) AS chiffre_affaires
FROM fact_orders f
JOIN dim_produits p
ON f.produit_id = p.produit_id
GROUP BY p.category
ORDER BY chiffre_affaires DESC;