use food_delivery_capstone_db
db.createCollection("customers")
db.createCollection("restaurants")
db.createCollection("delivery_partners")
db.createCollection("orders")

db.customers.insertMany([
{
customer_id: 1,
name: "Rahul Sharma",
city: "Hyderabad",
membership: "Gold",
phone: "9876543210"
},
{
customer_id: 2,
name: "Priya Reddy",
city: "Bangalore",
membership: "Silver",
phone: "9876543211"
},
{
customer_id: 3,
name: "Amit Kumar",
city: "Mumbai",
membership: "Gold",
phone: null
},
{
customer_id: 4,
name: "Sneha Patel",
city: "Chennai",
membership: "Bronze",
phone: "9876543213"
},
{
customer_id: 5,
name: "Arjun Verma",
city: "Delhi",
membership: "Silver",
phone: "9876543214"
}
])

db.restaurants.insertMany([
{
restaurant_id: 101,
name: "Spice Hub",
city: "Hyderabad",
cuisine: "Indian",
rating: 4.5
},
{
restaurant_id: 102,
name: "Pizza Corner",
city: "Bangalore",
cuisine: "Italian",
rating: 4.2
},
{
restaurant_id: 103,
name: "Green Bowl",
city: "Chennai",
cuisine: "Healthy",
rating: 4.7
},
{
restaurant_id: 104,
name: "Burger Street",
city: "Mumbai",
cuisine: "Fast Food",
rating: 3.9
},
{
restaurant_id: 105,
name: "Royal Tandoor",
city: "Delhi",
cuisine: "Indian",
rating: 4.8
}
])

db.delivery_partners.insertMany([
{
partner_id: 201,
partner_name: "FastMove Logistics",
city: "Hyderabad",
rating: 4.4
},
{
partner_id: 202,
partner_name: "QuickShip",
city: "Bangalore",
rating: 4.1
},
{
partner_id: 203,
partner_name: "SpeedKart",
city: "Mumbai",
rating: 4.6
},
{
partner_id: 204,
partner_name: "DoorDash India",
city: "Delhi",
rating: 4.0
}
])

db.orders.insertMany([
{
order_id: 1001,
customer_id: 1,
restaurant_id: 101,
partner_id: 201,
items: [
{ item_name: "Biryani", quantity: 2, price: 250 },
{ item_name: "Kebab", quantity: 1, price: 180 }
],
order_amount: 680,
payment: {
mode: "UPI",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 35,
order_rating: 5
},
{
order_id: 1002,
customer_id: 2,
restaurant_id: 102,
partner_id: 202,
items: [
{ item_name: "Pizza", quantity: 1, price: 500 },
{ item_name: "Garlic Bread", quantity: 1, price: 150 }
],
order_amount: 650,
payment: {
mode: "Card",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 42,
order_rating: 4
},
{
order_id: 1003,
customer_id: 3,
restaurant_id: 104,
partner_id: 203,
items: [
{ item_name: "Burger", quantity: 2, price: 180 },
{ item_name: "Fries", quantity: 1, price: 120 }
],
order_amount: 480,
payment: {
mode: "Cash",
status: "Pending"
},
order_status: "Pending",
delivery_time_minutes: null,
order_rating: null
},
{
order_id: 1004,
customer_id: 4,
restaurant_id: 103,
partner_id: null,
items: [
{ item_name: "Salad Bowl", quantity: 1, price: 350 }
],
order_amount: 350,
payment: {
mode: "UPI",
status: "Failed"
},
order_status: "Cancelled",
delivery_time_minutes: null,
order_rating: null
},
{
order_id: 1005,
customer_id: 5,
restaurant_id: 105,
partner_id: 204,
items: [
{ item_name: "Tandoori Chicken", quantity: 1, price: 600 },
{ item_name: "Naan", quantity: 2, price: 60 }
],
order_amount: 720,
payment: {
mode: "UPI",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 50,
order_rating: 5
},
{
order_id: 1006,
customer_id: 1,
restaurant_id: 101,
partner_id: 201,
items: [
{ item_name: "Paneer Curry", quantity: 1, price: 300 },
{ item_name: "Roti", quantity: 4, price: 25 }
],
order_amount: 400,
payment: {
mode: "Card",
status: "Success"
},
order_status: "Delivered",
delivery_time_minutes: 30,
order_rating: 4
}
])

