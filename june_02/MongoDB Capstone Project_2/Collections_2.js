use edtech_capstone_db;
db.createCollection("learners")
db.createCollection("courses")
db.createCollection("enrollments")
db.createCollection("instructors")

db.learners.insertMany([
{
learner_id: 1,
name: "Rahul Sharma",
city: "Hyderabad",
experience_years: 2,
goal: "Data Engineer",
phone: "9876543210"
},
{
learner_id: 2,
name: "Priya Reddy",
city: "Bangalore",
experience_years: 4,
goal: "AI Engineer",
phone: "9876543211"
},
{
learner_id: 3,
name: "Amit Kumar",
city: "Mumbai",
experience_years: 1,
goal: "Data Analyst",
phone: null
},
{
learner_id: 4,
name: "Sneha Patel",
city: "Chennai",
experience_years: 6,
goal: "ML Engineer",
phone: "9876543213"
},
{
learner_id: 5,
name: "Farhan Ali",
city: "Delhi",
experience_years: 3,
goal: "Cloud Engineer",
phone: "9876543214"
},
{
learner_id: 6,
name: "Meera Nair",
city: "Pune",
experience_years: 0,
goal: "AI Engineer",
phone: null
}
])

db.instructors.insertMany([
{
instructor_id: 101,
instructor_name: "Abdullah Khan",
expertise: ["AI", "Data Engineering", "Cloud"],
rating: 4.9
},
{
instructor_id: 102,
instructor_name: "Neha Singh",
expertise: ["Power BI", "SQL", "Analytics"],
rating: 4.6
},
{
instructor_id: 103,
instructor_name: "Ravi Kumar",
expertise: ["Python", "Machine Learning"],
rating: 4.7
}
])

db.courses.insertMany([
{
course_id: 201,
course_name: "Data Engineering with Azure",
category: "Data Engineering",
instructor_id: 101,
price: 15000,
level: "Intermediate",
tools: ["SQL", "Python", "Azure Data Factory", "Databricks"]
},
{
course_id: 202,
course_name: "AI Engineer Roadmap",
category: "Artificial Intelligence",
instructor_id: 101,
price: 20000,
level: "Beginner",
tools: ["Python", "OpenAI", "Vector DB", "LangChain"]
},
{
course_id: 203,
course_name: "Power BI for Business",
category: "Analytics",
instructor_id: 102,
price: 8000,
level: "Beginner",
tools: ["Power BI", "Excel", "SQL"]
},
{
course_id: 204,
course_name: "Machine Learning Practical",
category: "Machine Learning",
instructor_id: 103,
price: 12000,
level: "Intermediate",
tools: ["Python", "Scikit-learn", "Pandas"]
},
{
course_id: 205,
course_name: "Cloud AI Engineer",
category: "Cloud",
instructor_id: 101,
price: 18000,
level: "Advanced",
tools: ["Azure", "AWS", "GCP", "AI Services"]
}
])

db.enrollments.insertMany([
{
enrollment_id: 1001,
learner_id: 1,
course_id: 201,
enrollment_date: ISODate("2026-01-10"),
payment: {
amount: 15000,
mode: "UPI",
status: "Success"
},
progress: {
completed_modules: 8,
total_modules: 10,
completion_percent: 80
},
quiz_scores: [75, 82, 88],
status: "Active"
},
{
enrollment_id: 1002,
learner_id: 2,
course_id: 202,
enrollment_date: ISODate("2026-01-15"),
payment: {
amount: 20000,
mode: "Card",
status: "Success"
},
progress: {
completed_modules: 10,
total_modules: 10,
completion_percent: 100
},
quiz_scores: [90, 92, 95],
status: "Completed"
},
{
enrollment_id: 1003,
learner_id: 3,
course_id: 203,
enrollment_date: ISODate("2026-02-01"),
payment: {
amount: 8000,
mode: "Cash",
status: "Pending"
},
progress: {
completed_modules: 3,
total_modules: 8,
completion_percent: 37.5
},
quiz_scores: [60, 65],
status: "Active"
},
{
enrollment_id: 1004,
learner_id: 4,
course_id: 204,
enrollment_date: ISODate("2026-02-10"),
payment: {
amount: 12000,
mode: "UPI",
status: "Success"
},
progress: {
completed_modules: 6,
total_modules: 12,
completion_percent: 50
},
quiz_scores: [78, 80, 85],
status: "Active"
},
{
enrollment_id: 1005,
learner_id: 5,
course_id: 205,
enrollment_date: ISODate("2026-03-05"),
payment: {
amount: 18000,
mode: "Card",
status: "Failed"
},
progress: {
completed_modules: 0,
total_modules: 12,
completion_percent: 0
},
quiz_scores: [],
status: "Payment Failed"
},
{
enrollment_id: 1006,
learner_id: 6,
course_id: 202,
enrollment_date: ISODate("2026-03-12"),
payment: {
amount: 20000,
mode: "UPI",
status: "Success"
},
progress: {
completed_modules: 2,
total_modules: 10,
completion_percent: 20
},
quiz_scores: [55],
status: "Active"
}
])
