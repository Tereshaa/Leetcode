# Write your MySQL query statement below
select c.id,c.movie,c.description,c.rating
from cinema c
where id%2!=0 and description!="boring"
order by rating desc