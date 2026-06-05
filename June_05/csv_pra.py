import csv
with open("employees.csv","r") as file:
    reader=csv.reader(file)

    for row in reader:
        print(row)

with open("employees.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)

    for row in reader:
        print(row[1]) # display employees name

##Count Employees
count=0
with open("employees.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        count+=1
print(count)

#Highest salary
highest=0
with open("employees.csv","r") as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        salary=int(row[3])
        if salary>highest:
            highest=salary
print("Highest salary",highest)

#Lowest
low=999999
with open("employees.csv","r") as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        salary=int(row[3])
        if salary<low:
            low=salary
print("Lowest salary",low)

#Average
total=0
count=0
with open("employees.csv","r") as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        total+=int(row[3])
        count+=1
avg=total/count
print("Average salary",avg)

#Total salary
total=0
with open("employees.csv","r") as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        total+=int(row[3])
print("Total salary",total)

#Hyderabad employees
with open("employees.csv","r") as file:
    data = csv.reader(file)
    next(data)
    for row in data:
         if row[4]=="Hyderabad":
             print(row[1])
#AI Engineering
with open("employees.csv","r") as file:
    data = csv.reader(file)
    next(data)
    for row in data:
         if row[2]=="AI Engineering":
             print(row[1])

#Earning above 80000
with open("employees.csv","r") as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        if int(row[3])>80000:
            print(row[1],row[3])