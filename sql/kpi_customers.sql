-- ==========================================
-- KPI CLIENTS
-- ==========================================


-- 1. Nombre total de clients

SELECT
    COUNT(customer_id) AS nombre_clients
FROM dim_customers;



-- 2. Top 10 clients par chiffre d'affaires

SELECT
    customer_id,
    SUM(total_amount) AS chiffre_affaires

FROM fact_orders

GROUP BY customer_id

ORDER BY chiffre_affaires DESC

LIMIT 10;



-- 3. Dépense moyenne par client

SELECT
    ROUND(
        SUM(total_amount)::numeric
        /
        COUNT(DISTINCT customer_id),
        2
    ) AS depense_moyenne_client

FROM fact_orders;



-- 4. Clients les plus actifs

SELECT
    customer_id,
    COUNT(order_id) AS nombre_commandes

FROM fact_orders

GROUP BY customer_id

ORDER BY nombre_commandes DESC

LIMIT 10;



-- 5. Chiffre d'affaires moyen par client

SELECT
    ROUND(
        (SUM(total_amount)
        /
        COUNT(DISTINCT customer_id))::numeric,
        2
    ) AS ca_moyen_par_client

FROM fact_orders;



-- 6. Segmentation clients

SELECT
    customer_id,

    SUM(total_amount) AS chiffre_affaires,


    CASE
        WHEN SUM(total_amount) > 50000 THEN 'VIP'
        WHEN SUM(total_amount) > 20000 THEN 'REGULIER'
        ELSE 'STANDARD'
    END AS segment_client


FROM fact_orders

GROUP BY customer_id

ORDER BY chiffre_affaires DESC;



-- 7. Synthèse segmentation

SELECT

    segment_client,

    COUNT(*) AS nombre_clients,

    SUM(chiffre_affaires) AS chiffre_affaires_total


FROM
(

    SELECT

        customer_id,

        SUM(total_amount) AS chiffre_affaires,


        CASE
            WHEN SUM(total_amount) > 50000 THEN 'VIP'
            WHEN SUM(total_amount) > 20000 THEN 'REGULIER'
            ELSE 'STANDARD'
        END AS segment_client


    FROM fact_orders

    GROUP BY customer_id

) AS segmentation

GROUP BY segment_client

ORDER BY chiffre_affaires_total DESC;
LIMIT 20;