USE retail_capstone_db;

INSERT INTO customers (customer_id, customer_name, city, state, gender, membership_type) 
VALUES
(1,'Arjun','Chennai','Tamil Nadu','Male', 'Premium'),
(2,'Priya','Chennai','Tamil Nadu','Female','Gold'),
(3,'Karthik','Bangalore','Karnataka','Male','Silver'),
(4,'Sneha','Mumbai','Maharashtra','Female','Premium'),
(5,'Rahul','Mumbai','Maharashtra','Male','Silver'),
(6,'Divya','Chennai','Tamil Nadu','Female','Gold'),
(7,'Aakash','Delhi','Delhi','Male','Premium'),
(8,'Meera','Bangalore','Karnataka','Female','Silver'),
(9,'Vikram','Kolkata','West Bengal','Male','Gold'),
(10,'Ananya','Chennai','Tamil Nadu','Female','Silver');

INSERT INTO products (product_id, product_name, category, price) VALUES
(1,  'iPhone 15 Pro','Electronics',89999.00),
(2,  'Samsung Galaxy S24','Electronics',74999.00),
(3,  'Sony WH-1000XM5','Electronics',24999.00),
(4,  'Nike Air Max 270','Footwear',7999.00),
(5,  'Adidas Ultraboost 23','Footwear',9499.00),
(6,  'Puma Sports Backpack','Footwear',1999.00),
(7,  'Slim Jeans','Clothing',3499.00),
(8,  'Casual T-Shirt','Clothing',799.00),
(9,  'Philips Air Fryer','Kitchen',6999.00),
(10, 'Prestige Pressure Cooker','Kitchen',2199.00);

INSERT INTO orders (order_id, customer_id, order_date, order_status) VALUES
(1001, 1,  '2024-03-01', 'Delivered'), 
(1002, 1,  '2024-03-20', 'Delivered'),
(1003, 2,  '2024-03-05', 'Delivered'), 
(1004, 2,  '2024-04-01', 'Cancelled'),
(1005, 3,  '2024-03-10', 'Delivered'), 
(1006, 3,  '2024-04-18', 'Shipped'),
(1007, 4,  '2024-03-15', 'Delivered'), 
(1008, 4,  '2024-04-05', 'Shipped'), 
(1009, 5,  '2024-03-22', 'Delivered'),
(1010, 6,  '2024-03-28', 'Cancelled'),
(1011, 6,  '2024-04-10', 'Processing'), 
(1012, 7,  '2024-04-02', 'Shipped'), 
(1013, 8,  '2024-04-08', 'Delivered'),
(1014, 9,  '2024-04-12', 'Processing'), 
(1015, 10, '2024-04-15', 'Delivered');

INSERT INTO order_items (item_id, order_id, product_id, quantity) VALUES
(1,  1001, 1,  1),
(2,  1001, 3,  1),
(3,  1002, 9,  1),
(4,  1003, 2,  1),
(5,  1003, 8,  3),
(6,  1004, 7,  1),
(7,  1005, 4,  1),
(8,  1005, 6,  2),
(9,  1006, 5,  1),
(10, 1007, 4,  1),
(11, 1007, 10, 1),
(12, 1008, 5,  2),
(13, 1009, 9,  1),
(14, 1010, 8,  2),
(15, 1010, 6,  1),
(16, 1011, 7,  1),
(17, 1012, 1,  1),
(18, 1012, 2,  1),
(19, 1013, 10, 2),
(20, 1014, 3,  1);

INSERT INTO payments (payment_id, order_id, payment_mode, payment_status, amount) VALUES
(2001, 1001, 'UPI','Success',  89999.00),
(2002, 1002, 'Credit Card', 'Success',  24999.00),
(2003, 1003, 'Net Banking', 'Success',  74999.00),
(2004, 1004, 'Debit Card',  'Refunded',  3499.00),
(2005, 1005, 'UPI','Success',  17498.00),
(2006, 1006, 'Credit Card', 'Pending',   9499.00),
(2007, 1007, 'UPI','Success',   7999.00),
(2008, 1008, 'Debit Card',  'Pending',   9499.00),
(2009, 1009, 'COD','Success',   6999.00),
(2010, 1010, 'Credit Card', 'Failed', 2998.00),
(2011, 1011, 'Net Banking', 'Pending',3499.00),
(2012, 1012, 'UPI','Success', 97998.00),
(2013, 1013, 'Debit Card','Success',2199.00),
(2014, 1014, 'Credit Card', 'Failed',9499.00),
(2015, 1015, 'UPI', 'Success',  10798.00);

INSERT INTO deliveries (delivery_id, order_id, delivery_partner, delivery_status, delivery_city) VALUES
(3001, 1001, 'BlueDart', 'Delivered','Chennai'),
(3002, 1002, 'DTDC','Delivered','Chennai'),
(3003, 1003, 'Delhivery','Delivered','Chennai'),
(3004, 1004, 'Ekart','Returned','Chennai'),
(3005, 1005, 'BlueDart','Delivered','Bangalore'),
(3006, 1006, 'DTDC','Out for Delivery', 'Bangalore'),
(3007, 1007, 'Delhivery', 'Delivered','Mumbai'),
(3008, 1008, 'Ekart','Out for Delivery', 'Mumbai'),
(3009, 1009, 'BlueDart','Delivered','Mumbai'),
(3010, 1010, 'DTDC','Returned', 'Chennai'),
(3011, 1011, 'Delhivery', 'Pending','Chennai'),
(3012, 1012, 'Ekart','Out for Delivery', 'Delhi'),
(3013, 1013, 'BlueDart','Delivered','Bangalore'),
(3014, 1014, 'DTDC','Pending','Kolkata'),
(3015, 1015, 'Delhivery', 'Delivered','Chennai');

