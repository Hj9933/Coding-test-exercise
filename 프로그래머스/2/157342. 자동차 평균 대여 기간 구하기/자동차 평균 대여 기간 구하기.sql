-- 코드를 입력하세요
SELECT CAR_ID, round(AVG(datediff(end_date,start_date)+1),1) as AVERAGE_DURATION
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
having average_duration >= 7
order by average_duration desc, car_id desc