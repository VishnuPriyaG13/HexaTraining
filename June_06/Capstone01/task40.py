import csv

while True:
    print("\n===== E-Commerce Order Analytics System =====")
    print("1. View Orders")
    print("2. Revenue Analysis")
    print("3. Product Analysis")
    print("4. City Analysis")
    print("5. Export Reports")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        with open("orders.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)
    elif choice == 2:
        total_revenue = 0
        highest_order = 0
        lowest_order = float('inf')
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

                if revenue > highest_order:
                    highest_order = revenue

                if revenue < lowest_order:
                    lowest_order = revenue

        average_order = total_revenue / count

        print("Total Revenue:", total_revenue)
        print("Highest Order Value:", highest_order)
        print("Lowest Order Value:", lowest_order)
        print("Average Order Value:", round(average_order, 2))

    elif choice == 3:
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

        print("Products and Quantity Sold")
        for product, quantity in quantity_sold.items():
            print(product, ":", quantity)

        top_product = max(quantity_sold, key=quantity_sold.get)

        print("Most Sold Product:", top_product)

    elif choice == 4:
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

        print("Revenue By City")
        for city, revenue in city_revenue.items():
            print(city, ":", revenue)

        top_city = max(city_revenue, key=city_revenue.get)

        print("Top Revenue Generating City:", top_city)

    elif choice == 5:
        total_orders = 0
        total_revenue = 0

        with open("orders.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                quantity = int(row[5])
                price = int(row[6])

                total_orders += 1
                total_revenue += quantity * price

        with open("sales_summary_report.txt", "w") as report:
            report.write("Total Orders : " + str(total_orders) + "\n")
            report.write("Total Revenue : " + str(total_revenue))

        print("sales_summary_report.txt generated successfully.")

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
