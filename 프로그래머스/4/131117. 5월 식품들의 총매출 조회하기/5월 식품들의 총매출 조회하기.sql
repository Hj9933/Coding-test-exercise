-- 코드를 입력하세요
SELECT prod.product_id as PRODUCT_ID, prod.product_name as PRODUCT_NAME, sum(prod.price*ord.amount) as TOTAL_SALES
from food_product as prod
join food_order as ord
on prod.product_id = ord.product_id
where year(ord.produce_date) = 2022 and month(ord.produce_date) = 5
group by prod.product_id
order by sum(prod.price*ord.amount) desc, prod.product_id
