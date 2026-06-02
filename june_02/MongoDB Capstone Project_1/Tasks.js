db.customers.find()
db.restaurants.find()
db.customers.find({}, { name:1, city:1, membership:1, _id:0 })
db.customers.find({city:'Hyderabad'})
db.customers.find({membership:'Gold'})
db.restaurants.find({rating: {$gt:4.5}})
db.orders.find({order_amount:{$gt:500}})
db.orders.find({order_status:"Cancelled"})
db.orders.find({order_status:"Delivered"})
db.customers.find({phone:null})

db.orders.find({order_amount: {$gte:400,$lte:700}})
db.customers.find({city: {$in:["Hyderabad","Delhi","Mumbai"]}})
db.restaurants.find({cuisine:{$in:["Indian","Fast Food"]}})
db.orders.find({"payment.status":{$ne:"Success"}})
db.orders.find({delivery_time_minutes: null})
db.orders.find({order_rating: {$gte:4}})
db.restaurants.find({city: {$ne:["Bangalore","Chennai"]}})

db.orders.find({"items.item_name":"Biryani"})
db.orders.find({"items.item_name":"Pizza"})
db.orders.find({"items.quantity":{$gt:1}})
db.orders.find({"items.price": {$gt:300}})
db.orders.find({},{order_id:1,items:1,_id:0})

db.restaurants.find().sort({rating:-1})
db.restaurants.find().sort({rating:-1}).limit(3)
db.orders.find().sort({order_amount:-1})
db.delivery_partners.find().sort({rating:-1})

db.customers.updateOne({customer_id:1},{$set:{membership:"Platinum"}})
db.restaurants.updateOne({restaurent_id:104},{$set:{rating:4.1}})
db.orders.updateOne({order_id:1003},{$set:{order_status:"Delivered"}})
db.orders.updateOne({order_id:1003},{$set:{delivery_time_minutes:45}})
db.customers.updateMany({},{$set:{active:true}})
db.customers.updateMany({},{$unset:{active:""}})
db.orders.updateOne({order_id:1006},{$push:{items:{item_name:"Curd Rice",quantity:1,price:120}}})

db.orders.deleteMany({order_status:"Cancelled"})
db.restaurants.deleteMany({rating:{$lt:4.0}})

db.customers.countDocuments()
db.orders.countDocuments()
db.orders.countDocuments({order_status:"Delivered"})
db.orders.countDocuments({"payment.status":"Failed"}
db.customers.distinct("city")
db.restaurants.distinct("cuisine")
db.orders.distinct("payment.mode")

db.orders.aggregate([{$group:{_id:"$payment.mode",total_revenue:{$sum:"$order_amount"}}},
                     {$project:{_id:0,payment_mode:"$_id",total_revenue:1}}])
db.orders.aggregate([{$group:{_id:"$order_status",total_revenue:{$sum:"$order_amount"}}},
                     {$project:{_id:0,order_status:"$_id",total_revenue:1}}])
db.orders.aggregate([{$match:{order_status:"Delivered"}},
                     {$group:{_id:null,avg_delivery_time:{$avg:"$delivery_time_minutes"}}}])
db.orders.aggregate([{$group:{_id:"$customer_id",total_orders:{$sum:1},total_amount:{$sum:"$order_amount"}}},
                     {$project:{_id:0,customer_id:"$_id",total_orders:1,total_amount:1}}])
db.orders.aggregate([{$group:{_id:"$restaurant_id",total_orders:{$sum:1},total_revenue:{$sum:"$order_amount"}}},
                     {$project:{_id:0,restaurant_id:"$_id",total_orders:1,total_revenue:1}}])
db.orders.aggregate([{$match:{order_rating:{$ne:null}}},{$group:{_id:"$restaurant_id",
                    avg_rating:{$avg:"$order_rating"}}},{$project:{_id:0,restaurant_id:"$_id",avg_rating:1}}])
db.orders.aggregate([{$group:{_id:"$customer_id",total_spending:{$sum:"$order_amount"}}},{
                    $match:{total_spending:{$gt:700}}},{$project:{_id:0,customer_id:"$_id",total_spending:1}}])

db.orders.aggregate([
  { $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "customer_info"
  }},
  { $unwind: "$customer_info" },
  { $project: {
      _id: 0,
      order_id: 1,
      customer_name: "$customer_info.name",
      city: "$customer_info.city",
      order_amount: 1,
      order_status: 1
  }}
])

db.orders.aggregate([
  {$lookup: {
    from:"restaurants",
    localField:"restaurant_id",
    foreignField:"restaurant_id",
    as:"restaurant_info"
  }},
  {$unwind:"$restaurant_info"},
  {$project:{
    _id:0,
    order_id:1,
    restaurant_name: "$restaurant_info.name",
    cuisine: "$restaurant_info.cuisine",
    order_amount: 1
  }}
])

db.orders.aggregate([
  { $lookup: {
      from: "delivery_partners",
      localField: "partner_id",
      foreignField: "partner_id",
      as: "partner_info"
  }},
  { $unwind: {
      path: "$partner_info",
      preserveNullAndEmptyArrays: true
  }},
  { $project: {
      _id: 0,
      order_id: 1,
      partner_name: "$partner_info.partner_name",
      delivery_time: "$delivery_time_minutes",
      order_status: 1
  }}
])

db.orders.aggregate([
  { $lookup: {
      from: "customers",
      localField: "customer_id",
      foreignField: "customer_id",
      as: "cust"
  }},
  { $lookup: {
      from: "restaurants",
      localField: "restaurant_id",
      foreignField: "restaurant_id",
      as: "rest"
  }},
  { $lookup: {
      from: "delivery_partners",
      localField: "partner_id",
      foreignField: "partner_id",
      as: "part"
  }},
  { $unwind: "$cust" },
  { $unwind: "$rest" },
  { $unwind: {
      path: "$part",
      preserveNullAndEmptyArrays: true
  }},
  { $project: {
      _id: 0,
      order_id: 1,
      customer_name: "$cust.name",
      restaurant_name: "$rest.name",
      cuisine: "$rest.cuisine",
      partner_name: "$part.partner_name",
      order_amount: 1,
      payment_mode: "$payment.mode",
      payment_status: "$payment.status",
      order_status: 1,
      delivery_time: "$delivery_time_minutes",
      rating: "$order_rating"
  }}
])
