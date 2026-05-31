-- 최초 세대의 대장균들에게 '세대(=DEPTH)'를 1로 설정
WITH RECURSIVE GEN
AS (
    SELECT ID, PARENT_ID, 1 AS DEPTH 
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL -- 부모가 없으니 1세대

    UNION ALL

    SELECT CHILD.ID, CHILD.PARENT_ID, GEN.DEPTH + 1 -- 그 다음 세대(CHILD라고 지정함)부터는 +1 하나씩 해줌
    FROM ECOLI_DATA CHILD
    JOIN GEN ON CHILD.PARENT_ID = GEN.ID -- 부모 ID가 윗 세대 ID와 동일하면 세대(DEPTH)정보 get해와서 위 SELECT문처럼 +1해주면 그 놈은 그 다음 세대가 되.
),

CHILD
AS (
    SELECT A.ID, COUNT(B.ID) NUM 
    FROM ECOLI_DATA A
    LEFT JOIN ECOLI_DATA B
    ON A.ID=B.PARENT_ID -- A가 부모, B가 자식
    GROUP BY A.ID
)

-- 최종 결과를 구하는 쿼리
SELECT COUNT(*) AS COUNT, A.DEPTH AS GENERATION
FROM GEN A
JOIN CHILD B ON A.ID = B.ID -- GEN과 CHILD를 ID로 조인
WHERE B.NUM = 0 -- 자식이 없는 개체만 필터링
GROUP BY A.DEPTH -- 세대별로 그룹화
ORDER BY A.DEPTH; -- 세대 순으로 정렬