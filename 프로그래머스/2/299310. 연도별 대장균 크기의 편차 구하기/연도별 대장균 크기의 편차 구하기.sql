with max_diff as (select YEAR(differentiation_date) as YEAR, max(size_of_colony) as max_year
                 from ecoli_data
                 group by year)
                 
select b.YEAR, b.max_year-a.size_of_colony as YEAR_DEV, a.ID
from ecoli_data as a
join max_diff as b
on YEAR(a.differentiation_date) = b.year
order by b.year, year_dev

