create database if not exists order_insights;
use order_insights;

create table customers (
    customer_id     int auto_increment primary key,
    name            varchar(100) not null,
    email           varchar(150) unique,
    region          varchar(50),
    created_at      timestamp default current_timestamp
);

create table orders (
    order_id        int auto_increment primary key,
    customer_id     int not null,
    order_date      date not null,
    expected_date   date not null,
    amount          decimal(10,2) not null,
    status          varchar(20) default 'placed',
    foreign key (customer_id) references customers(customer_id)
);

create table delivery_status (
    delivery_id     int auto_increment primary key,
    order_id        int not null,
    delivered_date  date,
    is_delayed      boolean default false,
    delay_days      int default 0,
    notes           varchar(255),
    foreign key (order_id) references orders(order_id)
);

insert into customers (name, email, region) values
('Asha Patel', 'asha@example.com', 'West'),
('Ravi Kumar', 'ravi@example.com', 'North'),
('Meena Iyer', 'meena@example.com', 'South'),
('John Carter', 'john@example.com', 'East'),
('Priya Nair', 'priya@example.com', 'South'),
('Vikram Singh', 'vikram@example.com', 'North'),
('Sara Thomas', 'sara@example.com', 'West'),
('Arjun Mehta', 'arjun@example.com', 'East'),
('Lena Fernandes', 'lena@example.com', 'South'),
('Karan Shah', 'karan@example.com', 'West'),
('Divya Reddy', 'divya@example.com', 'South'),
('Mohit Verma', 'mohit@example.com', 'North'),
('Ayesha Khan', 'ayesha@example.com', 'East'),
('Rohan Joshi', 'rohan@example.com', 'West');

insert into orders (customer_id, order_date, expected_date, amount, status) values
(1, '2026-06-01', '2026-06-05', 1500.00, 'delivered'),
(2, '2026-06-03', '2026-06-07', 800.00, 'delivered'), 
(3, '2026-06-10', '2026-06-13', 2200.00, 'pending'),
(1, '2026-06-12', '2026-06-15', 950.00, 'delivered'),
(4, '2026-06-14', '2026-06-18', 3000.00, 'delivered'),
(5, '2026-06-08', '2026-06-11', 1200.00, 'delivered'),
(6, '2026-06-09', '2026-06-12', 600.00, 'delivered'),
(7, '2026-06-11', '2026-06-15', 1750.00, 'delivered'),
(8, '2026-06-12', '2026-06-16', 450.00, 'delivered'),
(9, '2026-06-13', '2026-06-17', 2750.00, 'delivered'),
(2, '2026-06-14', '2026-06-16', 990.00, 'delivered'),
(10, '2026-06-15', '2026-06-18', 1100.00, 'delivered'),
(5, '2026-06-17', '2026-06-20', 1340.00, 'delivered'),
(6, '2026-06-18', '2026-06-21', 720.00, 'delivered'),
(11, '2026-06-19', '2026-06-22', 1980.00, 'delivered'),
(12, '2026-06-20', '2026-06-23', 2400.00, 'delivered'),
(3, '2026-06-18', '2026-06-21', 1600.00, 'delivered'),
(13, '2026-06-22', '2026-06-25', 880.00, 'delivered'),
(14, '2026-06-23', '2026-06-26', 1450.00, 'delivered'),
(4, '2026-06-24', '2026-06-27', 2050.00, 'delivered');   

insert into delivery_status (order_id, delivered_date, is_delayed, delay_days, notes) values
(1, '2026-06-08', true, 3, 'Courier delay'),
(2, '2026-06-07', false, 0, 'On time'),
(4, '2026-06-19', true, 4, 'Warehouse backlog'),
(5, '2026-06-25', true, 7, 'Address correction needed'),
(6, '2026-06-10', false, 0, 'Delivered a day early'),
(7, '2026-06-15', true, 3, 'Support unresponsive'),
(8, '2026-06-15', false, 0, 'On time'),
(9, '2026-06-17', false, 0, 'Box damaged in transit'),
(10, '2026-06-16', false, 0, 'Delivered ahead of schedule'),
(11, '2026-06-18', true, 2, 'Minor routing delay'),
(12, '2026-06-21', true, 3, 'Tracking system issue'),
(13, '2026-06-19', false, 0, 'On time'),
(14, '2026-06-21', false, 0, 'Wrong item sent, reshipped'),
(15, '2026-06-24', true, 2, 'Slight delay, acceptable'),
(16, '2026-06-23', false, 0, 'On time'),
(17, '2026-06-25', true, 4, 'Repeat delay for this customer'),
(18, '2026-06-25', false, 0, 'On time'),
(19, '2026-06-27', false, 0, 'Quality mismatch reported'),
(20, '2026-06-30', true, 3, 'Recurring delay pattern');

-- 3. crud operations 
select * from orders where customer_id = 1;

-- read: join orders with delivery status
select o.order_id, c.name, o.order_date, d.delivered_date, d.is_delayed
from orders o
join customers c on o.customer_id = c.customer_id
left join delivery_status d on o.order_id = d.order_id;

-- update: mark an order as delivered
update orders set status = 'delivered' where order_id = 3;

-- delete: remove a delivery status record (example)
delete from delivery_status where delivery_id = 99;

drop procedure if exists GetDelayedDeliveries;

delimiter //

create procedure GetDelayedDeliveries(in cust_id int)
begin
    select
        o.order_id,
        o.order_date,
        o.expected_date,
        d.delivered_date,
        d.delay_days,
        d.notes
    from orders o
    join delivery_status d on o.order_id = d.order_id
    where o.customer_id = cust_id
      and d.is_delayed = true;
end //

delimiter ;

call GetDelayedDeliveries(1);