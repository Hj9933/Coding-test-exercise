SELECT a.INGREDIENT_TYPE, sum(total_order) as TOTAL_ORDER
from icecream_info a
inner join first_half b
on a.flavor = b.flavor
group by a.ingredient_type
order by TOTAL_ORDER asc