-- 코드를 작성해주세요

SELECT
    e1.id AS id,
    COUNT(e2.id) AS child_count
FROM ecoli_data e1
    LEFT JOIN ecoli_data e2
        ON e1.id = e2.parent_id
GROUP BY 1
ORDER BY 1