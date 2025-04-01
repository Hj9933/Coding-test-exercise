select count(f.id) as fISH_COUNT
from fish_info as f
join fish_name_info as n
on f.fish_type = n.fish_type
where n.fish_name = 'BASS' or n.fish_name = 'SNAPPER'
