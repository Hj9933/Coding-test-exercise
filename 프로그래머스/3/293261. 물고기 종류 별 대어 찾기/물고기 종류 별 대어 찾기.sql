select a.ID, b.FISH_NAME, a.LENGTH
from fish_info as a
join fish_name_info as b 
on a.fish_type = b.fish_type
where (a.fish_type, a.length) in (select fish_type, max(length)
                               from fish_info
                               group by fish_type)
order by a.ID