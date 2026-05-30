Create Database

CREATE DATABASE retail_db;
use retail_db;

Table 1: Customers

create table customers
(
customer_id int,
customer_name varchar(50),
city varchar(50)
);

insert into customers
values
(1,'Priya','Coimbatore'),
(2,'Amit','Bangalore'),
(3,'Ravi','Mumbai');

Exercises: SELECT, WHERE, DISTINCT, IN,
BETWEEN, LIKE, ORDER BY

select * from customers

set sql_safe_updates=0;
update customers
set city='Chennai'
where custmor_id=1;
set sql_safe_updates=1;

set sql_safe_updates=0;
delete from customers
where city='Mumbai';
set sql_safe_updates=1;

Table 2: products

create table products
(
product_id int primary key,
product_name varchar(100),
category varchar(50),
price decimal(10,2),
stock_quantity int,
supplier_city varchar(50)
);

insert into products
values
(1,'Laptop','Electronics',550000,10,'Hyderabad');
select * from products
insert into products
values
(2,'Mobile','Electronics',220000,25,'Chennai');
select * from products

update products
set price=15000
where product_id=2;
select * from products

set sql_safe_updates=0;
delete from products
where supplier_city='Hyderabad';
set sql_safe_updates=1;
drop table products

CREATE TABLE products
(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock_quantity INT,
    supplier_city VARCHAR(30)
);
INSERT INTO products VALUES
(1,'Laptop','Electronics',55000,10,'Hyderabad'),
(2,'Mobile','Electronics',25000,25,'Bangalore'),
(3,'Printer','Electronics',18000,8,'Pune'),
(4,'Office Chair','Furniture',7500,15,'Mumbai'),
(5,'Desk','Furniture',12000,5,'Chennai'),
(6,'Notebook','Stationery',80,200,'Hyderabad'),
(7,'Pen','Stationery',20,500,'Delhi'),
(8,'Water Bottle','Accessories',500,50,'Bangalore');

select product_name,price
from products;

select distinct category from products
select * from products 
where category='Electronics';

select * from products 
where price>10000;

select * from products 
where stock_quantity < 20;

select * from products 
where category='Electronics' and price>20000;

select * from products 
where supplier_city='Hyderabad' or supplier_city='Bangalore';

select * from products 
where not category='Electronics';

select * from products 
where supplier_city in ('Hyderabad','Delhi');

select * from products
where price between 500 and 20000;

select * from products
where product_name like '%P';

select * from products
where product_name like 'P%';

select * from products
where product_name like '%top%';

select product_name as Product,
price as Productprice from products;

select * from products order by price;
select * from products order by price desc;

select count(*) from products;
select count(*) from products
where category='Electronics';
select sum(price) from products;

select 
count(*) as Totalproducts,
sum(price) as Totalprice,
avg(price) as Averageprice,
max(price) as Maximumprice,
min(price) as Minimumprice
from products;

select category,
count(*) as Productcount from products
group by category;

select category,
sum(price) as TotalPrice from products
group by category;
