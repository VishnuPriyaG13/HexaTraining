create database if not exists supply_chain_db;
use supply_chain_db;

create table suppliers (
    supplier_id int auto_increment primary key,
    name varchar(100) not null,
    contact_email varchar(100),
    country varchar(50),
    lead_time_days int default 7
);

create table orders (
    order_id        int auto_increment primary key,
    supplier_id     int not null,
    product_id      int not null,
    quantity        int not null,
    order_date      date not null default (current_date),
    delivery_date   date,
    status          enum('pending', 'shipped', 'delivered', 'delayed') default 'pending',
    foreign key (supplier_id) references suppliers(supplier_id)
);

create table inventory (
    product_id          int auto_increment primary key,
    product_name        varchar(100) not null,
    stock_level         int not null default 0,
    reorder_threshold   int not null default 10,
    last_updated        timestamp default current_timestamp on update current_timestamp
);

insert into suppliers (name, contact_email, country, lead_time_days) values
('global supplies co.',  'contact@globalsupplies.com',  'india',         5),
('rapid logistics ltd.', 'info@rapidlogistics.com',     'germany',       3),
('eastpack trading',     'sales@eastpack.com',          'china',         10),
('ameritrade goods',     'support@ameritrade.com',      'usa',           7),
('swift cargo inc.',     'hello@swiftcargo.com',        'uae',           4);

insert into inventory (product_name, stock_level, reorder_threshold) values
('wireless mouse',     120,  20),
('usb-c hub',          8,    15),
('mechanical keyboard',45,   10),
('hdmi cable',         200,  30),
('laptop stand',       5,    10),
('webcam hd',          60,   15),
('monitor 24 inch',    12,   8);

insert into orders (supplier_id, product_id, quantity, order_date, delivery_date, status) values
(1, 2, 50,  '2025-06-01', '2025-06-06', 'delivered'),
(2, 5, 30,  '2025-06-05', '2025-06-08', 'delayed'),
(3, 1, 100, '2025-06-07', '2025-06-17', 'shipped'),
(4, 6, 20,  '2025-06-10', '2025-06-17', 'pending'),
(5, 3, 75,  '2025-06-11', '2025-06-15', 'shipped'),
(1, 7, 15,  '2025-06-12', '2025-06-17', 'pending'),
(2, 4, 200, '2025-06-13', '2025-06-16', 'delivered');

select * from orders;
select * from suppliers;
select * from inventory;
## all orders with supplier name (join)
select 
    o.order_id,
    s.name          as supplier_name,
    i.product_name,
    o.quantity,
    o.order_date,
    o.delivery_date,
    o.status
from orders o
join suppliers s  on o.supplier_id = s.supplier_id
join inventory i  on o.product_id  = i.product_id;

##only delayed or pending orders
select 
    o.order_id,
    s.name as supplier_name,
    o.status,
    o.delivery_date
from orders o
join suppliers s on o.supplier_id = s.supplier_id
where o.status in ('delayed', 'pending');

## products with stock below reorder threshold
select 
    product_id,
    product_name,
    stock_level,
    reorder_threshold
from inventory
where stock_level < reorder_threshold;

##update queries
set sql_safe_updates = 0;
update orders
set status = 'delayed'
where delivery_date < current_date
and status not in ('delivered', 'delayed');
set sql_safe_updates = 1;

set sql_safe_updates=0;
update inventory
set stock_level = stock_level - 50
where product_id = 2;
set sql_safe_updates=1;

set sql_safe_updates=0;
update suppliers
set lead_time_days = 6
where name = 'global supplies co.';
set sql_safe_updates=1;

delete from orders
where order_id = 7 and status = 'delivered';
select * from orders;

-- stored procedure: auto_reorder()
delimiter $$
create procedure auto_reorder()
begin
    -- declare variables
    declare done        int default 0;
    declare v_product_id    int;
    declare v_stock         int;
    declare v_threshold     int;
    declare v_supplier_id   int;

    -- cursor to loop through all inventory items
    declare inventory_cursor cursor for
        select 
            i.product_id,
            i.stock_level,
            i.reorder_threshold,
            o.supplier_id
        from inventory i
        join orders o on i.product_id = o.product_id
        where i.stock_level < i.reorder_threshold
        order by o.order_id desc
        limit 1;

    declare continue handler for not found set done = 1;

    open inventory_cursor;

    reorder_loop: loop
        fetch inventory_cursor into v_product_id, v_stock, v_threshold, v_supplier_id;
        
        if done = 1 then
            leave reorder_loop;
        end if;

        -- insert a new order for low stock product
        insert into orders (supplier_id, product_id, quantity, order_date, delivery_date, status)
        values (
            v_supplier_id,
            v_product_id,
            v_threshold * 2,            -- order double the threshold quantity
            current_date,
            date_add(current_date, interval 7 day),
            'pending'
        );

    end loop;

    close inventory_cursor;
end$$

delimiter ;

-- check which products are below threshold before calling
select product_id, product_name, stock_level, reorder_threshold
from inventory
where stock_level < reorder_threshold;

-- call the procedure
call auto_reorder();

-- verify new orders were inserted
select 
    o.order_id,
    s.name          as supplier_name,
    i.product_name,
    o.quantity,
    o.status,
    o.order_date,
    o.delivery_date
from orders o
join suppliers s  on o.supplier_id = s.supplier_id
join inventory i  on o.product_id  = i.product_id
where o.status = 'pending'
order by o.order_id desc;

-- trigger: fire auto_reorder after every inventory update

delimiter $$

create trigger check_reorder
after update on inventory
for each row
begin
    -- only fire if stock level actually dropped below threshold
    if new.stock_level < new.reorder_threshold 
    and old.stock_level >= old.reorder_threshold then
        call auto_reorder();
    end if;
end$$

delimiter ;

-- test the trigger

-- simulate stock dropping below threshold for webcam hd (product_id = 6)
update inventory
set stock_level = 5
where product_id = 6;

-- verify trigger fired and new order was created
select 
    o.order_id,
    i.product_name,
    o.quantity,
    o.status,
    o.order_date
from orders o
join inventory i on o.product_id = i.product_id
where i.product_id = 6
order by o.order_id desc
limit 1;

-- check procedure exists
show procedure status where db = 'supply_chain_db';

-- check trigger exists
show triggers from supply_chain_db;

