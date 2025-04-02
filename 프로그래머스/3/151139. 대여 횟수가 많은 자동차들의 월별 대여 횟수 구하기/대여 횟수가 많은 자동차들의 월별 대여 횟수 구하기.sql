-- 코드를 입력하세요
SELECT month(start_date) as MONTH, CAR_ID, count(car_id) as RECORD
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where car_id in (select car_id
                 from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 where MONTH(start_date) >= 8 and MONTH(start_date) <= 10 
                 group by car_id
                 having count(car_id) >= 5)
                 and month(start_date) >= 8 and month(start_date) <= 10
group by MONTH(start_date), car_id
order by month(start_date) asc, car_id desc