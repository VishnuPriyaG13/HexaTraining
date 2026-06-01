USE retail_capstone_db;

select * from customers;
select customer_name,city,membership_type from customers;
select * from products order by price desc;
select * from customers where city='Hyderabad';
select * from customers where membership_type='Gold';
select * from products where price between 500 and 5000;
select * from products where category in ('Electronics', 'Fashion');
select * from orders where order_date > '2026-01-01';
select * from payments where payment_mode='UPI';
select * from deliveries where delivery_status='Pending';

select count(*) as total_customers from customers;
select count(*) as total_orders from orders;
select count(*) as total_products from products;
select sum(amount) as total_revenue from payments where payment_status='Success';
select avg(amount) as average_payment from payments;
select max(amount) as highest_payment from payments;
select min(amount) as lowest_payment from payments;
select city,count(*) as total_customers from customers group by city; 
select category,count(*) as total_products from products group by category;
select order_status,count(*) as total_orders from orders group by order_status;

select c.customer_name,o.order_id,o.order_date
from customers c
join orders o on c.customer_id=o.customer_id;

select oi.order_id,p.product_name,oi.quantity,p.price
from order_items oi
join products p on p.product_id=oi.product_id;

select c.customer_name,p.product_name,oi.quantity,o.order_date
from customers c
join orders o on c.customer_id=o.customer_id
join order_items oi on o.order_id=oi.order_id
join products p on oi.product_id=p.product_id;

select o.order_id,p.payment_mode,p.payment_status,p.amount
from orders o
join payments p on o.order_id=p.order_id;

select o.order_id,d.delivery_partner,d.delivery_status
from orders o
join deliveries d on o.order_id=d.order_id;

select c.customer_name,
c.city,
o.order_id,
o.order_date,
p.product_name,
p.category,
oi.quantity,
p.price,
py.payment_status,
d.delivery_status
from customers c
join orders o on c.customer_id = o.customer_id
join order_items oi on o.order_id = oi.order_id
join products p on oi.product_id = p.product_id
join payments py on o.order_id   = py.order_id
join deliveries d on o.order_id  = d.order_id;

select c.city,sum(py.amount) as total_revenue
from customers c
join payments py on py.order_id in(select order_id from orders where customer_id=c.customer_id)
group by c.city; 

select c.customer_name,sum(py.amount) as total_revenue
from customers c
join orders o on c.customer_id=o.customer_id
join payments py on o.order_id=py.order_id
group by c.customer_name;

select p.product_name,sum(oi.quantity) as total_quantity
from products p
join order_items oi on p.product_id=oi.product_id
group by p.product_name;

select p.category, sum(py.amount) as total_revenue
from products p
join order_items oi on p.product_id = oi.product_id
join orders o on oi.order_id = o.order_id
join payments py on o.order_id = py.order_id
group by p.category;

select c.customer_name,count(o.order_id) as total_order
from customers c
join orders o on c.customer_id=o.customer_id
group by c.customer_name;

select c.customer_name,count(o.order_id) as total_order
from customers c
join orders o on c.customer_id=o.customer_id
group by c.customer_name
having count(o.order_id)>1;

select p.category, sum(py.amount) as total_revenue
from products p
join order_items oi on p.product_id = oi.product_id
join orders o on oi.order_id = o.order_id
join payments py on o.order_id = py.order_id
group by p.category
having sum(py.amount)>10000;

select city,count(customer_id) as total_customers
from customers
group by city
having count(customer_id)>2;

select p.product_name,sum(oi.quantity) as total_sold
from products p
join order_items oi on p.product_id=oi.product_id
group by p.product_name
having sum(oi.quantity)>3;

select customer_name from customers
where customer_id in(
select distinct customer_id from orders);

select customer_name from customers
where customer_id not in(
select distinct customer_id from orders);

select product_name from products
where product_id not in(
select distinct product_id from order_items);

select order_id from orders
where order_id in(
select order_id from payments
where amount>(select avg(amount)from payments)
);

select customer_name from customers
where customer_id=(
select customer_id from orders
where order_id=(
select order_id from payments
where amount=(select max(amount) from payments)
)
);

select product_name,price from products
where price>(select avg(price) from products);

select customer_name from customers
where customer_id in (
select customer_id from orders
where order_id in(
select order_id from order_items
where product_id in(
select product_id from products
where category='Electronics')
)
);

select * from orders
where order_id in(
select order_id from payments
where payment_status='Success');

select * from orders
where order_id not in(
select order_id from deliveries
where delivery_status='Delivered');

select c.customer_name,sum(py.amount) as total_spending
from customers c
join orders o on c.customer_id=o.customer_id
join payments py on o.order_id=py.order_id
group by c.customer_name
having sum(py.amount)>(select avg(total) from(
select sum(py2.amount) as total from orders o2
join payments py2 on o2.order_id=py2.order_id
group by o2.customer_id) as avg_spending
);

select * from orders
where order_id not in(select order_id from payments);

select * from orders
where order_id not in(select order_id from deliveries);

select * from payments 
where amount=0 or amount is null;

select o.order_id, o.customer_id, o.order_status, py.payment_status
from orders o
join payments py on o.order_id = py.order_id
where o.order_status = 'Cancelled'
and py.payment_status = 'Success';

select o.order_id, o.customer_id, o.order_status, py.payment_status
from orders o
join payments py on o.order_id = py.order_id
where o.order_status = 'Delivered'
and py.payment_status = 'Failed';

select * from order_items
where product_id not in(select product_id from products);

select * from orders
where customer_id not in(select customer_id from customers);


