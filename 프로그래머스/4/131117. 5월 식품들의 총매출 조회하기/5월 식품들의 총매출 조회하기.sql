-- 코드를 입력하세요
SELECT
    fp.product_id,
    fp.product_name,
    SUM(fo.amount * fp.price) AS totoal_sales -- 총매출=주문량*가격
FROM FOOD_ORDER AS fo
    JOIN FOOD_PRODUCT AS fp USING(product_id)
WHERE 1=1
    AND YEAR(fo.produce_date) = 2022
    AND MONTH(fo.produce_date) = 05
    -- AND EXTRACT(YEAR FROM O.PRODUCE_DATE) = 2022 AND EXTRACT(MONTH FROM O.PRODUCE_DATE)=5
    
GROUP BY fp.product_id, fp.product_name
ORDER BY totoal_sales DESC, fp.product_id ASC