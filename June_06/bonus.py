import csv
# Generate a CSV file for high-value orders (revenue > 50,000)
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    with open("high_value_orders.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        for row in reader:
            quantity = int(row[5])
            price = int(row[6])
            revenue = quantity * price
            if revenue > 50000:
                writer.writerow(row)

print("high_value_orders.csv generated successfully.")

#Generate electronics_orders.csv
with open("orders.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    with open("electronics_orders.csv", "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        for row in reader:
            category = row[4]
            if category.lower() == "electronics":
                writer.writerow(row)
print("electronics_orders.csv generated successfully.")
