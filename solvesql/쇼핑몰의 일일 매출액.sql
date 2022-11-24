select
  order_purchase_timestamp as dt,
  round(sum(payment_value), 2) as revenue_daily
from
  (
    select
      order_id,
      strftime('%Y-%m-%d', order_purchase_timestamp, 'localtime') as order_purchase_timestamp
    from
      olist_orders_dataset
    where
      order_purchase_timestamp > '2018-01-01'
  ) as t1
  join (
    select
      order_id,
      payment_value
    from
      olist_order_payments_dataset
  ) as t2 on (t1.order_id = t2.order_id)
group by
  order_purchase_timestamp
order by
  order_purchase_timestamp;