select bike_id
from rental_history 
where rent_at>='2021-01-01' and return_at<'2021-02-01'
group by bike_id
having sum(distance)>=50000
order by bike_id;