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
      day,
      max(total_bill) as max_total
    from
      tips
    group by
      day
  ) as t1 on (
    tips.total_bill = t1.max_total
    and tips.day = t1.day
  )