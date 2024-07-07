-- 코드를 입력하세요
SELECT date_format(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, ifnull(USER_Id,null) as USER_ID, SALES_AMOUNT
from online_sale 
where year(sales_date) = 2022 and month(sales_date) = 3
union all
select SALES_DATE, PRODUCT_ID, null, SALES_AMOUNT
from offline_sale 
where year(sales_date) = 2022 and month(sales_date) = 3
order by sales_date, product_id, user_id