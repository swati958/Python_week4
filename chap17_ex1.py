# make a function
#divide

#print(divide(4,2))  
#print(dibide(4,0))   please don't divide by zero
#print(divide('4',2))   please input numbers only


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print("nmber must be int or floats")
    except :
        print("unexcepted error")

print(divide(10,'2'))