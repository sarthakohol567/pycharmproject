
try:
    a=int(input("ENter a Number:"))
    b=int(input("ENter an other Number:"))
    res=a/b
    print(res)
except ZeroDivisionError:
    print("Can not divide with 0")
except ValueError:
    print("Pass valid input")
except Exception as e:
    print(e)
else:
    print("This blovk run when there s no exception")
    print("Division result:",res)
finally:
    print("This block always run")