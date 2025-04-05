-- 코드를 입력하세요
select b.REST_ID, b.REST_NAME, b.FOOD_TYPE, b.FAVORITES, b.ADDRESS, round(avg(a.review_score),2) as SCORE
from rest_review as a
join rest_info as b
on a.rest_id = b.rest_id
where left(b.address,2) = '서울'
group by b.rest_id
order by score desc, favorites desc
