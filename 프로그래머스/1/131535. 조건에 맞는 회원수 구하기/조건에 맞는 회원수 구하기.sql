-- 코드를 입력하세요
SELECT count(user_id) as 'USERS'
from user_info
where joined between date('2021-01-01') and date('2021-12-31')
and age >= 20 and age <= 29