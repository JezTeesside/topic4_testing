def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Invalid input"
    except:
        return "Invalid case"
print(divide(10,2))
print(divide(10,0))
print(divide("4","b"))
