select
  order_delivered_carrier_date as delivered_carrier_date,
  count(*) as orders
from
  (
    select
      strftime(
        '%Y-%m-%d',
        order_delivered_carrier_date,
        'localtime'
      ) as order_delivered_carrier_date,
      strftime(
        '%Y-%m-%d',
        order_delivered_customer_date,
        'localtime'
      ) as order_delivered_customer_date
    from
      olist_orders_dataset
    where
      order_delivered_carrier_date > '2017-01'
      and order_delivered_carrier_date < '2017-02'
      and order_delivered_customer_date is null
  ) as t1
group by
  order_delivered_carrier_date
order by
  delivered_carrier_date;