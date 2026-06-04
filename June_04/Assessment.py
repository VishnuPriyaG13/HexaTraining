#Dataset 1-->Employee Salary List

salaries=[45000,55000,65000,75000,85000]
#Display all salaries
print(salaries)

#find max and min salary
print(max(salaries))
print(min(salaries))

#total salary
print(sum(salaries))

#average salary
length=len(salaries)
avg=sum(salaries)/length
print(avg)

#Add 95000, 105000 to the list
salaries.append(95000)
salaries.append(105000)
print(salaries)

#remove 55000
salaries.remove(55000)
print(salaries)

#sort salaries ascending
salaries.sort()
print(salaries)

#sort salaries in descending
salaries.sort(reverse=True)
print(salaries)

#second highest salary(By converting the list into descending order the second highest salary will be the data in the index number 1
#so just print the data in index number 1. That will the output
print("Second Highest salary: ",salaries[1])

#Display salaries greater than 70000
print("Salaries greater than 70000: ")
for salary in salaries:
    if salary>70000:
        print(salary)

#DataSet 2-->Employee Record(Tuple)

employee=(
    101,
    "Rahul Sharma",
    "Data Engineer",
    75000
)
print(employee)
print(employee[1]) #Display name
print(employee[2]) #Display department

emp_id,name,department,salary=employee
print("Employee_id: ",emp_id)
print("Name: ",name)
print("Department: ",department)
print("Salary: ",salary)

print("Length: ",len(employee))
print("First Element: ",employee[0])
print("Last Element: ",employee[-1])

#Dataset 3-->Batch Students(Set)
batch_a = {
"Rahul",
"Priya",
"Amit",
"Sneha",
"Farhan"
}
batch_b = {
"Priya",
"Sneha",
"Neha",
"Arjun",
"Farhan"
}
#Find common students
res=batch_a.intersection(batch_b)
print(res)

#Find students only in batch_a
res1=batch_a.difference(batch_b)
print(res1)

#Find students only in batch_b
res2=batch_b.difference(batch_a)
print(res2)

#unique students
unique_students=batch_a.union(batch_b)
print(unique_students)

#Students present in one batch but notin both
res=batch_a.symmetric_difference(batch_b)
print(res)

#DataSet 4-->Employee (Dictionary)

employee_info = {
"employee_id": 101,
"name": "Rahul Sharma",
"department": "Data Engineering",
"salary": 75000,
"city": "Hyderabad"
}
print("Name: "+employee_info["name"])
print("Department: "+employee_info["department"])
print("City: "+employee_info["city"])

employee_info["experience"]=5
print(employee_info)

employee_info["salary"]=85000
print(employee_info)

employee_info.pop("city")
print(employee_info)

print(employee_info.keys())
print(employee_info.values())
print(employee_info.items())

#DataSet 5-->List of Dictionaries

employees = [
{
"id": 101,
"name": "Rahul",
"department": "IT",
"salary": 50000
},
{
"id": 102,
"name": "Priya",
"department": "HR",
"salary": 70000
},
{
"id": 103,
"name": "Amit",
"department": "IT",
"salary": 60000
},
{
"id": 104,
"name": "Sneha",
"department": "Finance",
"salary": 80000
},
{
"id": 105,
"name": "Farhan",
"department": "IT",
"salary": 90000
}
]
#show employees name
for emp in employees:
    print(emp["name"])
#employees belongs to IT
for emp in employees:
    if emp["department"] == "IT":
        print(emp["name"])

highest=max(employees,key=lambda x:x["salary"])
print("Highest salary: ",highest["salary"])

lowest=min(employees,key=lambda x:x["salary"])
print("Lowest salary: ",lowest["salary"])

avg_salary=sum(emp["salary"] for emp in employees)/len(employees)
print("Average salary: ",avg_salary)

total_salary=sum(emp["salary"] for emp in employees)
print("Total salary: ",total_salary)

for emp in employees:
    if emp["salary"]>70000:
        print(emp["name"], emp["salary"])

#Count employees in IT
count=0

for emp in employees:
    if emp["department"]=="IT":
        count+=1
print("IT Employees: ",count)

#Employee names sorted by salary descending
sort_emp=sorted(employees,key=lambda x:x["salary"],reverse=True)
for emp in sort_emp:
    print(emp["name"], emp["salary"])

#Second highest salary employee
sec_hig=sort_emp[1]
print(sec_hig)

#departments without duplicates
dep={emp ["department"] for emp in employees}
print(dep)



