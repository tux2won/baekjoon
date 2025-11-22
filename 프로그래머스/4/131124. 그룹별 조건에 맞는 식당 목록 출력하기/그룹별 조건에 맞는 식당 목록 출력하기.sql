-- 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회

WITH base AS (
    SELECT
        member_id,
        member_name,
        review_text,
        review_date,
        COUNT(*) OVER (PARTITION BY member_id) AS review_cnt
    FROM member_profile AS m
        JOIN rest_review AS r
            USING(member_id)
    ORDER BY review_cnt
), rnk AS (
    SELECT 
        *,
        DENSE_RANK() OVER(ORDER BY review_cnt DESC) AS review_rnk
    FROM base
)
SELECT
    member_name,
    review_text,
    DATE_FORMAT(review_date, '%Y-%m-%d') AS review_date
FROM rnk
WHERE review_rnk = 1
ORDER BY 3, 2