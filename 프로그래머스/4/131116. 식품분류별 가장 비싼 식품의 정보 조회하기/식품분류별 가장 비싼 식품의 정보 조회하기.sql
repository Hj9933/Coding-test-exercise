-- 코드를 입력하세요
SELECT a.CATEGORY, a.price as MAX_PRICE, a.PRODUCT_NAME
from food_product as a
join (select category, max(price) as price, product_name
    from food_product
    where category in ('과자', '국', '김치', '식용유')
    group by category) as b
where a.category=b.category and a.price=b.price
order by max_price desc