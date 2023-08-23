def greater(n):
    if(n > 50):
        return n
numbers = [20, 10, 60, 70, 5, 90, 110]
result = filter(greater, numbers)
print(list(result))