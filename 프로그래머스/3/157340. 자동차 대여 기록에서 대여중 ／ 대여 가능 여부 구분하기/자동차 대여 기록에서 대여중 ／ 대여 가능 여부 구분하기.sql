-- 코드를 입력하세요
SELECT CAR_ID,
if (max(date(start_date) <= '2022-10-16' and date(end_date) >= '2022-10-16'), '대여중', '대여 가능') as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
order by car_id desc