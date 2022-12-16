select round(avg(s),2)
from (select day, sum(total_bill)  as s
from tips
group by day) as t1