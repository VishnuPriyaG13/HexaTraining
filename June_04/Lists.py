#List
cities=["Hyderabad","Mumbai","Delhi"]

print(cities[0])
print(cities[1])
print(cities[2])

# Negative Indexing
print(cities[-1])
print(cities[-2])

#update an element
cities[1]="Bangalore"
print(cities)

#Append
cities.append("Chennai")
print(cities)

#insert
cities.insert(1,"Pune")
print(cities)

cities.extend(["Kochin","Pondi"])
print(cities)

#remove
cities.remove("Pune")
print(cities)

#pop
cities.pop()
print(cities)

cities.pop(1)
print(cities)

#del --->deleting the elements
del cities[0]
print(cities)

#clear--> deletes the entier list data
#cities.clear()
#print(cities)

#To find length of the list
print(len(cities))

# Check Membership
print("Mumbai" in cities)
print("Chennai" in cities)

print(cities.index("Kochin"))

#To sort the List
cities.sort()
print(cities)


