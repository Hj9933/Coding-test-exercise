-- 코드를 입력하세요
SELECT a.FLAVOR
from first_half as a
join (
select SHIPMENT_ID, FLAVOR, sum(total_order) as TOTAL_ORDER
from july
group by flavor) as b
on a.flavor = b.flavor
order by (a.TOTAL_ORDER + b.TOTAL_ORDER) desc
limit 3