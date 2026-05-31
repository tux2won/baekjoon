-- WITH RECURSIVE: CTE 안에서 자기 자신을 참조 가능함

WITH RECURSIVE generation_info AS (
    SELECT
        ecoli.id AS id,
        ecoli.parent_id AS parent_id,
        1 AS generation
    FROM ecoli_data AS ecoli
    WHERE 1=1
        AND ecoli.parent_id IS NULL

    UNION ALL

    SELECT
        child_ecoli.id AS id,
        child_ecoli.parent_id AS parent_id,
        parent_generation.generation + 1 AS generation
    FROM ecoli_data AS child_ecoli
        JOIN generation_info AS parent_generation
            ON child_ecoli.parent_id = parent_generation.id
),
child_count AS (
    SELECT
        parent_ecoli.id AS id,
        COUNT(child_ecoli.id) AS child_count
    FROM ecoli_data AS parent_ecoli
        LEFT JOIN ecoli_data AS child_ecoli
            ON parent_ecoli.id = child_ecoli.parent_id
    GROUP BY parent_ecoli.id
)

SELECT
    COUNT(*) AS count,
    generation_info.generation AS generation
FROM generation_info AS generation_info
    JOIN child_count AS child_count
        ON generation_info.id = child_count.id
WHERE 1=1
    AND child_count.child_count = 0
GROUP BY generation
ORDER BY generation;