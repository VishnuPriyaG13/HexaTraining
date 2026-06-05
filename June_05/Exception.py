#Generic Exception
try:
    a=10
    b=0
    result=a/b
    print(result)

except:
    print("error")

print("Program completed")

#Specific Exception
try:
    a=10
    b=0
    result=a/b
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

###
try:
    age=int(input("Enter age: "))
    print(age)
except ValueError:
    print("Please enter a numeric value")

#Multiple Exceptions
try:
    age=int(input("Enter age: "))
    print(100/age)
except ValueError:
    print("Please enter a numeric value")
except ZeroDivisionError:
    print("Age cannot be zero")

#Exception Object
try:
    num=int("abc")
    print(num)
except Exception as e:
    print(e)

#Else Block
try:
    num=10
    print(num)
except:
    print("Error")
else:
    print("Success")

#Finally
try:
    print(10/0)
except:
    print("Error")
finally:
    print("Connection closed")

#Raise Error
salary=-1000
if salary<0:
    raise ValueError("Salary cannot be negative")

