def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
         return "You are dividing by zero and is meaningless"

print(divide(1,0))

print("End of Program")