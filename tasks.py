import csv
#Read  the csv file
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#Print all records
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    print("All Records: \n")
    for row in reader:
        print(row)


#Count total orders
count = 0
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        count += 1
print("Total Orders :", count)

#Calculate total revenue
total_revenue=0
with open("orders.csv", "r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        quantity =int(row[5])
        price =int(row[6])
        order_value = quantity * price
        total_revenue += order_value
print("Total Revenue :", total_revenue)

#highest order value
highest_order=0
with open("orders.csv", "r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        quantity =int(row[5])
        price =int(row[6])
        order_value = quantity * price
        if order_value > highest_order:
            highest_order = order_value
print("Highest Order Value :", highest_order)

#lowest order value
lowest_order = float('inf')
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        quantity = int(row[5])
        price = int(row[6])
        order_value = quantity * price
        if order_value < lowest_order:
            lowest_order = order_value
print("Lowest Order Value :", lowest_order)

#Average order value
total_revenue = 0
count = 0
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        quantity = int(row[5])
        price = int(row[6])
        order_value = quantity*price
        total_revenue += order_value
        count += 1
average_order = total_revenue/count
print("Average Order Value :", round(average_order,2))

#Display All Unique Customers
customers=set()
with open("orders.csv", "r") as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        customers.add(row[1])
print("Unique Customers :")
for customer in customers:
    print(customer)

#Count Unique Customers
print("Number of Unique Customers =", len(customers))

#Find Customer with Highest Purchase Amount
highest_purchase = 0
top_customer = ""
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        customer_name = row[1]
        quantity = int(row[5])
        price = int(row[6])
        purchase_amount = quantity * price
        if purchase_amount > highest_purchase:
            highest_purchase = purchase_amount
            top_customer = customer_name
print("Customer with Highest Purchase Amount:", top_customer)
print("Purchase Amount:", highest_purchase)

#Count Orders by Product
product_count = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1
print("Orders by Product:")
for product, count in product_count.items():
    print(product, ":", count)

#Calculate Revenue by Product
product_revenue = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        quantity = int(row[5])
        price = int(row[6])
        revenue = quantity * price
        if product in product_revenue:
            product_revenue[product] += revenue
        else:
            product_revenue[product] = revenue

print("Revenue by Product:")
for product, revenue in product_revenue.items():
    print(product, ":", revenue)

#Find Most Sold Product
quantity_sold = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        quantity = int(row[5])
        if product in quantity_sold:
            quantity_sold[product] += quantity
        else:
            quantity_sold[product] = quantity
most_sold_product = max(quantity_sold, key=quantity_sold.get)
print("Most Sold Product:", most_sold_product)
print("Quantity Sold:", quantity_sold[most_sold_product])

#Find Least Sold Product
min_quantity = min(quantity_sold.values())
least_sold_products = []
for product, quantity in quantity_sold.items():
    if quantity == min_quantity:
        least_sold_products.append(product)
print("Least Sold Products:", least_sold_products)
print("Quantity Sold:", min_quantity)

#Calculate Revenue by Category
category_revenue = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        category = row[4]
        quantity = int(row[5])
        price = int(row[6])
        revenue = quantity * price
        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue
print("Revenue by Category:")
for category, revenue in category_revenue.items():
    print(category, ":", revenue)

#Count Orders by City
city_count = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        city = row[2]
        if city in city_count:
            city_count[city] += 1
        else:
            city_count[city] = 1
print("Orders by City:")
for city, count in city_count.items():
    print(city, ":", count)

#Calculate Revenue by City
city_revenue = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        city = row[2]
        quantity = int(row[5])
        price = int(row[6])
        revenue = quantity * price
        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue
print("Revenue by City:")
for city, revenue in city_revenue.items():
    print(city, ":", revenue)

#Find City Generating Highest Revenue
highest_revenue_city = max(city_revenue, key=city_revenue.get)
print("City Generating Highest Revenue:", highest_revenue_city)
print("Revenue:", city_revenue[highest_revenue_city])

#Store All Product Names in a List and Sort Alphabetically
products=[]
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        if product not in products:
            products.append(product)
products.sort()
print("Product Names (Sorted Alphabetically):")
print(products)

#Store Unique Cities in a Set
cities = set()
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        city = row[2]
        cities.add(city)
print("Unique Cities:")
print(cities)

#Create Dictionary {city : revenue}
city_revenue = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        city = row[2]
        quantity = int(row[5])
        price = int(row[6])

        revenue = quantity * price
        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue
print("City Revenue:")
print(city_revenue)

#Create Dictionary {product : quantity_sold}
quantity_sold = {}
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[3]
        quantity = int(row[5])
        if product in quantity_sold:
            quantity_sold[product] += quantity
        else:
            quantity_sold[product] = quantity
print("Quantity Sold by Product:")
print(quantity_sold)

#calculate_total_revenue()
def calculate_total_revenue():
    total_revenue = 0

    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            quantity = int(row[5])
            price = int(row[6])
            revenue = quantity * price
            total_revenue += revenue
    return total_revenue
print("Total Revenue:", calculate_total_revenue())

#find_top_product()
def find_top_product():
    quantity_sold = {}
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            product = row[3]
            quantity = int(row[5])
            if product in quantity_sold:
                quantity_sold[product] += quantity
            else:
                quantity_sold[product] = quantity
    top_product = max(quantity_sold, key=quantity_sold.get)
    return top_product
print("Top Product:", find_top_product())

#find_top_city()
def find_top_city():
    city_revenue = {}
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            city = row[2]
            quantity = int(row[5])
            price = int(row[6])
            revenue = quantity * price
            if city in city_revenue:
                city_revenue[city] += revenue
            else:
                city_revenue[city] = revenue
    top_city = max(city_revenue, key=city_revenue.get)
    return top_city
print("Top City:", find_top_city())

#find_average_order_value()
def find_average_order_value():
    total_revenue = 0
    count = 0
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            quantity = int(row[5])
            price = int(row[6])
            revenue = quantity * price
            total_revenue += revenue
            count += 1
    average_order_value = total_revenue / count
    return average_order_value

print("Average Order Value:", round(find_average_order_value(), 2))

#Handle Missing CSV File
try:
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)

except FileNotFoundError:
    print("Error: orders.csv file not found.")

#Handle Invalid Quantity Values
try:
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                quantity = int(row[5])
                print(quantity)

            except ValueError:
                print("Invalid quantity value:", row[5])

except FileNotFoundError:
    print("Error: orders.csv file not found.")

#Handle Invalid Price Values
try:
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                price = int(row[6])
                print(price)

            except ValueError:
                print("Invalid price value:", row[6])
except FileNotFoundError:
    print("Error: orders.csv file not found.")

#NumPy
import numpy as np
order_values = []
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        quantity = int(row[5])
        price = int(row[6])
        revenue = quantity * price
        order_values.append(revenue)
order_array = np.array(order_values)
print(order_array)

total_revenue = np.sum(order_array)
print("Total Revenue:", total_revenue)

average_revenue = np.mean(order_array)
print("Average Revenue:", average_revenue)

max_revenue = np.max(order_array)
print("Maximum Revenue:", max_revenue)

min_revenue = np.min(order_array)
print("Minimum Revenue:", min_revenue)

std_deviation = np.std(order_array)
print("Standard Deviation:", round(std_deviation, 2))

#Pandas
import pandas as pd
df = pd.read_csv("orders.csv")
print(df)