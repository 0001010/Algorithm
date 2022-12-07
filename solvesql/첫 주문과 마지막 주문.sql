select min(order_purchase_timestamp) as first_order_date , max(order_purchase_timestamp)as last_order_date 
from(select strftime('%Y-%m-%d', order_purchase_timestamp, 'localtime') as order_purchase_timestamp 
from olist_orders_dataset) t1;