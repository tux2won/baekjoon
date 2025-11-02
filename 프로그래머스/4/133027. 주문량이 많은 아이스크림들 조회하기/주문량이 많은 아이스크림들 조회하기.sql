WITH base AS (
    SELECT
        flavor,
        total_order
    FROM first_half
    UNION ALL
    SELECT
        flavor,
        total_order
    FROM july
)
SELECT flavor
FROM base
GROUP BY flavor
ORDER BY SUM(total_order) DESC  -- ORDER BY 2 대신 명시적으로 SUM(total_order) 사용
LIMIT 3;