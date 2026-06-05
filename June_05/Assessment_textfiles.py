#Read and Display entire file
from Assessment import highest

with open(
    "Employees_ass.txt",
    "r"
) as file:
    print(file.read())

#Display file lineby line
with open(
    "Employees_ass.txt",
    "r"
) as file:
    for line in file:
        print(line.strip())

#Count total employees
with open(
    "Employees_ass.txt",
    "r"
) as file:
    count=len(file.readlines())
    print(count)

#Display only Employees name
with open(
    "Employees_ass.txt",
    "r"
) as file:
    for line in file:
        data=line.strip().split(",")
        print(data[1])

#Employees from Hyderabad
with open(
    "Employees_ass.txt",
    "r"
) as file:
    for line in file:
        data=line.strip().split(",")
        if data[4]=="Hyderabad":
            print(data[1])

#Employees from Bangalore
with open(
    "Employees_ass.txt",
    "r"
) as file:
    for line in file:
        data=line.strip().split(",")
        if data[4]=="Bangalore":
            print(data[1])

#Employees with salary greater than 80000
with open(
    "Employees_ass.txt",
    "r"
) as file:
    for line in file:
        data=line.strip().split(",")
        if int(data[3])>80000:
            print(data[1], data[3])

#Highest Salary
highest=0
with open(
    "Employees_ass.txt",
    "r"
) as file:
    for line in file:
        salary=int(line.strip().split(",")[3])
        if salary>highest:
            highest=salary
print("Highest salary: ",highest)

#Lowest salary
highest=0
with open(
    "Employees_ass.txt",
    "r"
) as file:
   salaries=[int(line.strip().split(",")[3]) for line in file]
print("Lowest Salary: ", min(salaries))

#Average salary
highest=0
with open(
    "Employees_ass.txt",
    "r"
) as file:
   salaries=[int(line.strip().split(",")[3]) for line in file]
avg=sum(salaries)/len(salaries)
print("Average salary: ", avg)

#Total salary payout
highest=0
with open(
    "Employees_ass.txt",
    "r"
) as file:
   salaries=[int(line.strip().split(",")[3]) for line in file]
print("Total salary payout: ",sum(salaries))

#Employees in AI Engineering
count=0
with open(
    "Employees_ass.txt",
    "r"
) as file:
     for line in file:
         if line.strip().split(",")[2]=="AI Engineering":
             count+=1
print("Employees in AI Engineering: ", count)

#Employees in data engineering
count=0
with open(
    "Employees_ass.txt",
    "r"
) as file:
     for line in file:
         if line.strip().split(",")[2]=="Data Engineering":
             count+=1
print("Employees in Data Engineering: ", count)

#Display employees in AI Engineering
with open(
    "Employees_ass.txt",
    "r"
) as file:
     for line in file:
         data=line.strip().split(",")
         if data[2]=="AI Engineering":
             print(data[1])

#create high_salary employees text
with open(
    "Employees_ass.txt",
    "r"
) as file, \
    open("high_salary_employees.txt","w") as out:
    for line in file:
        if int(line.strip().split(",")[3])>80000:
            out.write(line)
print("File created")

#Create Hyderabad employees.txt
with open(
    "Employees_ass.txt",
    "r"
) as file, \
    open("Hyderabad_employees.txt","w") as out:
    for line in file:
        if line.strip().split(",")[4] == "Hyderabad":
            out.write(line)
print("File created")

#count unique cities
cities=set()
with open(
    "Employees_ass.txt",
    "r"
)as file:
    for line in file:
        cities.add(line.strip().split(",")[4])
print("Unique Cities: ",len(cities))
for city in cities:
    print(city)

#Count employees by department
dept_count = {}

with open(
        "Employees_ass.txt", "r") as file:
    for line in file:
        dept = line.strip().split(",")[2]

        if dept in dept_count:
            dept_count[dept] += 1
        else:
            dept_count[dept] = 1

for dept, count in dept_count.items():
    print(dept, "=", count)

#Employee with highest salary
max_salary = 0
employee = ""

with open("Employees_ass.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        if int(data[3]) > max_salary:
            max_salary = int(data[3])
            employee = data[1]

print(employee)
print(max_salary)

#employee_report
with open("Employees_ass.txt", "r") as file:
    salaries = [int(line.strip().split(",")[3]) for line in file]

report = f"""
EMPLOYEE REPORT
------------------------
Total Employees : {len(salaries)}
Highest Salary  : {max(salaries)}
Lowest Salary   : {min(salaries)}
Average Salary  : {sum(salaries)/len(salaries)}
Total Salary    : {sum(salaries)}
"""

with open("employee_report.txt", "w") as file:
    file.write(report)

print("employee_report.txt created successfully")
