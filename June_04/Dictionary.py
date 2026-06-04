#Dictionary
customer={
    "customer_id":101,
    "name":"Rahul",
    "city":"Mumbai"
}
print(customer)

print(customer["name"])
print(customer["city"])

#safest way
print(customer.get("name"))
print(customer.get("city"))

#Add new key value pair
customer["Salary"]=75000
print(customer)

#update
customer["name"]="Rahul Sharma"
print(customer)

customer.pop("Salary")
print(customer)

del customer["city"]
print(customer)