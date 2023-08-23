# 1.try - except
# try:
#     numerator = 10
#     denominator = 0
#     result = numerator/denominator
#     print(result)
# except:
#     print("Error: denominator can not be 0")


# program to print reciprocal of a even number
# 2.try-except-else
try:
    n = int(input("Enter no: "))
    if n % 2 == 0:
        reciprocal = 1 / n
        print(reciprocal)
    else:
        print("Not an even number")
except ValueError:
    print("Invalid input! Please enter a valid number.")
