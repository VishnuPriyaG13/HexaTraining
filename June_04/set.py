#sets-->not allow duplicates

cities={"Hyderabad","Mumbai","Delhi","Pune"}
print(cities)

cities={"Hyderabad","Mumbai","Delhi","Pune","Mumbai"}
print(cities)

#Remove duplicates fro list
citi=["Hyderabad","Mumbai","Delhi","Pune","Mumbai"]
unique_cities=set(citi)
print(unique_cities)

cities.add("Chennai")
print(cities)

cities.update(["Chennai","Kochin"])
print(cities)

cities.remove("Delhi") # shows error when the data is not present in the set
print(cities)

cities.discard("Delhi") # No error when data is not present
print(cities)

#Union, Intersection
set1={"Python","SQL"}
set2={"MongoDB","Python"}
result1=set1.union(set2) # combine both sets and return without duplicates
print(result1)

result2=set1.intersection(set2) # common data between 2 sets
print(result2)

result3=set1.difference(set2) # difference between set 1 and set2 and returns set1 data only
print(result3)

result4=set1.symmetric_difference(set2) # difference between set1 and 2 and returns both sets data
print(result4)