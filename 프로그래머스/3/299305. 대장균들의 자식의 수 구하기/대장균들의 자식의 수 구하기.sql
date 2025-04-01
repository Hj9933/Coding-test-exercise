select a.ID, count(B.PARENT_ID) as CHILD_COUNT
from ecoli_data as a
left outer join ecoli_data as b
on a.id = b.parent_id
group by a.id 