use supply_chain_db

db.createCollection("shipment_logs")

db.shipment_logs.insertMany([
    {
        order_id: 1,
        event_type: "dispatched",
        timestamp: new Date("2025-06-01T08:00:00"),
        location: "mumbai warehouse",
        carrier: "bluedart",
        notes: "order picked up from supplier"
    },
    {
        order_id: 1,
        event_type: "in_transit",
        timestamp: new Date("2025-06-03T14:30:00"),
        location: "delhi hub",
        carrier: "bluedart",
        notes: "shipment in transit to destination"
    },
    {
        order_id: 1,
        event_type: "delivered",
        timestamp: new Date("2025-06-06T11:00:00"),
        location: "bangalore",
        carrier: "bluedart",
        notes: "delivered successfully"
    },
    {
        order_id: 2,
        event_type: "dispatched",
        timestamp: new Date("2025-06-05T09:00:00"),
        location: "berlin warehouse",
        carrier: "dhl",
        notes: "order dispatched from supplier"
    },
    {
        order_id: 2,
        event_type: "exception",
        timestamp: new Date("2025-06-07T16:00:00"),
        location: "frankfurt hub",
        carrier: "dhl",
        notes: "customs clearance delay"
    },
    {
        order_id: 3,
        event_type: "dispatched",
        timestamp: new Date("2025-06-07T10:00:00"),
        location: "shanghai warehouse",
        carrier: "fedex",
        notes: "order dispatched"
    },
    {
        order_id: 3,
        event_type: "in_transit",
        timestamp: new Date("2025-06-10T08:00:00"),
        location: "hong kong hub",
        carrier: "fedex",
        notes: "cleared customs, heading to destination"
    },
    {
        order_id: 4,
        event_type: "dispatched",
        timestamp: new Date("2025-06-10T12:00:00"),
        location: "new york warehouse",
        carrier: "ups",
        notes: "order dispatched from supplier"
    },
    {
        order_id: 5,
        event_type: "dispatched",
        timestamp: new Date("2025-06-11T07:00:00"),
        location: "dubai warehouse",
        carrier: "aramex",
        notes: "shipment dispatched"
    },
    {
        order_id: 5,
        event_type: "in_transit",
        timestamp: new Date("2025-06-13T09:00:00"),
        location: "abu dhabi hub",
        carrier: "aramex",
        notes: "in transit to india"
    }
])


db.shipment_logs.createIndex({ order_id: 1 })
db.shipment_logs.createIndex({ timestamp: -1 })
db.shipment_logs.createIndex({ event_type: 1, carrier: 1 })

db.shipment_logs.find({ order_id: 1 }).sort({ timestamp: 1 })
db.shipment_logs.find({ event_type: { $in: ["exception", "delayed"] } })
db.shipment_logs.find().sort({ timestamp: -1 }).limit(1)

db.shipment_logs.aggregate([
    { $group: { _id: "$event_type", count: { $sum: 1 } } },
    { $sort: { count: -1 } }
])

db.shipment_logs.getIndexes()
