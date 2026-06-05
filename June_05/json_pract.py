import json

from Assessment import highest

employees = [

    {
        "employee_id": 101,
        "name": "Rahul Sharma",
        "department": "Data Engineering",
        "salary": 75000,
        "city": "Hyderabad"
    },

    {
        "employee_id": 102,
        "name": "Priya Reddy",
        "department": "AI Engineering",
        "salary": 85000,
        "city": "Bangalore"
    },

    {
        "employee_id": 103,
        "name": "Amit Kumar",
        "department": "Data Engineering",
        "salary": 65000,
        "city": "Mumbai"
    },

    {
        "employee_id": 104,
        "name": "Sneha Patel",
        "department": "Data Science",
        "salary": 95000,
        "city": "Chennai"
    },

    {
        "employee_id": 105,
        "name": "Farhan Ali",
        "department": "Cloud Engineering",
        "salary": 80000,
        "city": "Delhi"
    }

]
with open(
    "employees.json","w") as file:
    json.dump(employees,file,indent=4)

print("JSON file created successfully")

with open("employees.json","r") as file:
    employees = json.load(file)
print(employees)

for employee in employees:
    print(employee)

for employee in employees:
    print(employee["name"])

print(len(employees))

highest_salary=0
for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
print(highest_salary)

###Exercise
# Employee with highest salary
highest=employees[0]
for employee in employees:
    if employee["salary"] > highest["salary"]:
        highest= employee
print(highest["name"]," ", highest["salary"])

#Average salary
total=0
for emp in employees:
    total+=emp["salary"]
avg=total/len(employees)
print("Average salary: ",avg)

#Data Engineering employees
for emp in employees:
    if emp["department"] == "Data Engineering":
        print(emp["name"])

#Employees earning more than 80000
for emp in employees:
    if emp["salary"] > 80000:
        print(emp["name"]," ",emp["salary"])

#Update salary on an Employee
for emp in employees:
    if emp["name"]=="Rahul Sharma":
        emp["salary"]=90000
with open("employees.json","w") as file:
    json.dump(employees,file,indent=4)
print("JSON file updated successfully")

#Add new employee
new_employee={
    "employee_id":106,
    "name":"Ravi",
    "department":"Data Engineering",
    "salary":70000,
    "city":"Chennai"
}
employees.append(new_employee)
with open("employees.json","w") as file:
    json.dump(employees,file,indent=4)
print("Employee added successfully")