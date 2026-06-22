use order_insights;
db.feedback.drop();

db.createCollection("feedback");

db.feedback.insertMany([
  {
    customer_id: 1,
    order_id: 1,
    feedback_text: "Delivery was late but the product quality was great.",
    rating: 4,
    tags: ["late_delivery", "good_quality"],
    submitted_at: new Date("2026-06-09")
  },
  {
    customer_id: 2,
    order_id: 2,
    feedback_text: "Arrived right on time, very happy.",
    rating: 5,
    tags: ["on_time"],
    submitted_at: new Date("2026-06-07")
  },
  {
    customer_id: 3,
    order_id: 3,
    feedback_text: "Still waiting, no updates on tracking.",
    rating: 2,
    tags: ["pending", "no_communication"],
    submitted_at: new Date("2026-06-14")
  },
  {
    customer_id: 1,
    order_id: 4,
    feedback_text: "Second order was also delayed, getting frustrating.",
    rating: 2,
    tags: ["late_delivery", "repeat_issue"],
    submitted_at: new Date("2026-06-20")
  },
  {
    customer_id: 4,
    order_id: 5,
    feedback_text: "Packaging was damaged on arrival despite being a week late.",
    rating: 1,
    tags: ["late_delivery", "damaged_packaging"],
    submitted_at: new Date("2026-06-26")
  },
  {
    customer_id: 5,
    order_id: 6,
    feedback_text: "Great experience, the courier even called ahead.",
    rating: 5,
    tags: ["on_time", "good_communication"],
    submitted_at: new Date("2026-06-11")
  },
  {
    customer_id: 6,
    order_id: 7,
    feedback_text: "Order was three days late and support didn't respond.",
    rating: 1,
    tags: ["late_delivery", "no_communication"],
    submitted_at: new Date("2026-06-13")
  },
  {
    customer_id: 7,
    order_id: 8,
    feedback_text: "Average experience, nothing special but no complaints either.",
    rating: 3,
    tags: ["neutral"],
    submitted_at: new Date("2026-06-15")
  },
  {
    customer_id: 8,
    order_id: 9,
    feedback_text: "Box was crushed but the item inside was fine.",
    rating: 3,
    tags: ["damaged_packaging", "good_quality"],
    submitted_at: new Date("2026-06-16")
  },
  {
    customer_id: 9,
    order_id: 10,
    feedback_text: "Fastest delivery I've had from this company, impressed.",
    rating: 5,
    tags: ["on_time", "fast_delivery"],
    submitted_at: new Date("2026-06-17")
  },
  {
    customer_id: 2,
    order_id: 11,
    feedback_text: "This time the order was two days late, unlike before.",
    rating: 3,
    tags: ["late_delivery", "repeat_customer"],
    submitted_at: new Date("2026-06-18")
  },
  {
    customer_id: 10,
    order_id: 12,
    feedback_text: "Tracking link never worked, had to call customer service.",
    rating: 2,
    tags: ["no_communication", "tracking_issue"],
    submitted_at: new Date("2026-06-19")
  },
  {
    customer_id: 5,
    order_id: 13,
    feedback_text: "Second order also arrived early, very reliable service.",
    rating: 5,
    tags: ["on_time", "repeat_customer"],
    submitted_at: new Date("2026-06-21")
  },
  {
    customer_id: 6,
    order_id: 14,
    feedback_text: "Wrong item was delivered, had to request a replacement.",
    rating: 1,
    tags: ["wrong_item"],
    submitted_at: new Date("2026-06-22")
  },
  {
    customer_id: 11,
    order_id: 15,
    feedback_text: "Decent packaging, delivery was a bit delayed but acceptable.",
    rating: 3,
    tags: ["late_delivery", "good_quality"],
    submitted_at: new Date("2026-06-23")
  },
  {
    customer_id: 12,
    order_id: 16,
    feedback_text: "Excellent service, the delivery person was very polite.",
    rating: 5,
    tags: ["on_time", "good_communication"],
    submitted_at: new Date("2026-06-24")
  },
  {
    customer_id: 3,
    order_id: 17,
    feedback_text: "Order finally arrived after a week of waiting.",
    rating: 2,
    tags: ["late_delivery", "repeat_issue"],
    submitted_at: new Date("2026-06-25")
  },
  {
    customer_id: 13,
    order_id: 18,
    feedback_text: "No issues at all, smooth process from order to delivery.",
    rating: 4,
    tags: ["on_time"],
    submitted_at: new Date("2026-06-27")
  },
  {
    customer_id: 14,
    order_id: 19,
    feedback_text: "Item quality did not match the description on the website.",
    rating: 2,
    tags: ["quality_mismatch"],
    submitted_at: new Date("2026-06-28")
  },
  {
    customer_id: 4,
    order_id: 20,
    feedback_text: "Another delayed order, this is becoming a pattern.",
    rating: 1,
    tags: ["late_delivery", "repeat_issue"],
    submitted_at: new Date("2026-06-29")
  }
]);

db.feedback.createIndex({ customer_id: 1 });
print("Indexes on feedback collection:");
db.feedback.getIndexes().forEach(idx => printjson(idx));
print("\nFeedback for customer_id = 1:");
db.feedback.find({ customer_id: 1 }).forEach(doc => printjson(doc));

print("\nAll feedback with rating <= 2 (unhappy customers):");
db.feedback.find({ rating: { $lte: 2 } }).forEach(doc => printjson(doc));

print("\nCount of feedback documents tagged 'late_delivery':");
print(db.feedback.countDocuments({ tags: "late_delivery" }));

print("\nCustomers with more than one feedback entry (repeat feedback):");
db.feedback.aggregate([
  { $group: { _id: "$customer_id", count: { $sum: 1 } } },
  { $match: { count: { $gt: 1 } } },
  { $sort: { count: -1 } }
]).forEach(doc => printjson(doc));

print("\nAverage rating across all feedback:");
db.feedback.aggregate([
  { $group: { _id: null, avg_rating: { $avg: "$rating" } } }
]).forEach(doc => printjson(doc));
