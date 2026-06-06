import csv

total_orders = 0
total_revenue = 0
highest_order = 0
lowest_order = float('inf')

city_revenue = {}
category_revenue = {}
quantity_sold = {}

with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        city = row[2]
        category = row[4]
        product = row[3]
        quantity = int(row[5])
        price = int(row[6])

        revenue = quantity * price

        total_orders += 1
        total_revenue += revenue

        if revenue > highest_order:
            highest_order = revenue

        if revenue < lowest_order:
            lowest_order = revenue

        # Revenue by city
        if city in city_revenue:
            city_revenue[city] += revenue
        else:
            city_revenue[city] = revenue

        # Revenue by category
        if category in category_revenue:
            category_revenue[category] += revenue
        else:
            category_revenue[category] = revenue

        # Quantity sold by product
        if product in quantity_sold:
            quantity_sold[product] += quantity
        else:
            quantity_sold[product] = quantity

average_order_value = total_revenue / total_orders

top_product = max(quantity_sold, key=quantity_sold.get)
top_city = max(city_revenue, key=city_revenue.get)

with open("sales_summary_report.txt", "w") as report:
    report.write("SALES SUMMARY REPORT\n")
    report.write("--------------------\n")
    report.write(f"Total Orders: {total_orders}\n")
    report.write(f"Total Revenue: {total_revenue}\n")
    report.write(f"Average Order Value: {average_order_value:.2f}\n")
    report.write(f"Highest Order Value: {highest_order}\n")
    report.write(f"Lowest Order Value: {lowest_order}\n\n")

    report.write("Revenue By City:\n")
    for city, revenue in city_revenue.items():
        report.write(f"{city}: {revenue}\n")

    report.write("\nRevenue By Category:\n")
    for category, revenue in category_revenue.items():
        report.write(f"{category}: {revenue}\n")

    report.write(f"\nTop Selling Product: {top_product}\n")
    report.write(f"Top Revenue Generating City: {top_city}\n")

print("sales_summary_report.txt generated successfully.")
