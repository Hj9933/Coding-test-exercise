select f.ID, f.LENGTH
from fish_info as f
order by f.length desc, f.id asc
limit 10