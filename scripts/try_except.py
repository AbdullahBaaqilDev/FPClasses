



x = "Mohammed"
y = 47

try:
    print(x + y)
except TypeError as error:
    x = 10
    print(f"x has changed error = ({error})")
    print(x + y)
else:
    print("printed successfully")


x = 10
y = 0

try:
    print(x / y)
except Exception as error:
    y = 5
    print(f"y = 5, error = ({error})")
    print(x / y)
else:
    print("printed successfully")
