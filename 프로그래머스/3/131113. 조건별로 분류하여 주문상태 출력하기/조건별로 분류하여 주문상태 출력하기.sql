-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE,'%Y-%m-%d') as OUT_DATE,
if(out_date <= '2022-05-01', '출고완료',(if(out_date > '2022-05-01', '출고대기', '출고미정'))) as 출고여부
from food_order
order by order_id