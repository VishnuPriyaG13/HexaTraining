#Tuple-->act as read only records

cities=("Hyderabad","Mumbai","Delhi","Chennai","Pune")
print(cities)

print(cities[0])
print(cities[1])

print(cities[-1])
print(cities[-2])

print(len(cities))

print(cities[1:4])

#Packing and Unpacking
#1
employee=(101,"Rahul",25000)
print(employee)
#2
emp_id,emp_name,emp_salary=employee
print(emp_id)
print(emp_name)
print(emp_salary)

#return multiple values
def get_employee():
    return 101,"Rahul",25000
result=get_employee()
print(result)

#Each row is represented as Tuple
record=(
    101,
    "Ravi",
    "Chennai",
    35000
)
print(record)

