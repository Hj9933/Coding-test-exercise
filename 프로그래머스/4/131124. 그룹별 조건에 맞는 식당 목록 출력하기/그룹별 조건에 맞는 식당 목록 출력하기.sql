-- 코드를 입력하세요
with reviews as (select member_id, count(*) as review_count
                 from rest_review
                 group by member_id
                 order by count(*) desc
                 limit 1)
select c.MEMBER_NAME, a.REVIEW_TEXT, date_format(a.review_date,'%Y-%m-%d') as REVIEW_DATE
from rest_review as a
join reviews as b
on b.member_id = a.member_id
join member_profile as c
on c.member_id = b.member_id
order by a.review_date, a.review_text