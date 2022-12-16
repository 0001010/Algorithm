select total_bill, tip, sex, smoker, day, time, size
from(select
  *, (select avg(total_bill) as avg_b from tips) as avg_b
from
  tips
where total_bill>=avg_b) as t1