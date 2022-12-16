select purchase_date, sum(success) as success, sum(fail) as fail
from (select
  strftime('%Y-%m-%d',order_purchase_timestamp , 'localtime') as purchase_date ,
  case
    when order_delivered_customer_date <= order_estimated_delivery_date then 1
    else 0
  end  as success,
  case
    when order_delivered_customer_date > order_estimated_delivery_date then 1
    else 0
  end  as fail
from
  olist_orders_dataset
where
  order_purchase_timestamp >= '2017-01-01'
  and order_purchase_timestamp < '2017-02-01') as t1

group by purchase_date;