-- 코드를 입력하세요
SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE-- max(PRICE) as PRICE
from food_product
order by price desc
limit 1

