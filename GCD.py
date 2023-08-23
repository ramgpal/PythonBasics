# Brute force approach
m = int(input("Enter first number\n"))
n = int(input("Enter 2nd number\n"))
# if m<n:
#     min = m
# else:
#     min = n
# for i in range (1, min+1):
#     if m%i==0 and n%i==0:
#         hcf = i
# print(hcf)

# Optimize approach -> Euclidean Algorithm
  # TC -> O(log(min))
if m < n:
    max = n
    min = m
else:
    max = m
    min = n
while(min != 0):
    temp = min
    min = max % min
    max = temp
print(max)