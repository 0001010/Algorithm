select
  total_bill,
  tip,
  sex,
  smoker,
  tips.day,
  time,
  size
from
  tips
  join (
    select
      day
    from
      tips
    group by
      day
    having
      sum(total_bill) >= 1500
  ) as t on (tips.day = t.day)