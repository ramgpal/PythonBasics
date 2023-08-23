m = int(input("Enter first number\n"))
n = int(input("Enter 2nd number\n"))
if m<n:
    min = m
else:
    min = n
for i in range (1, min+1):
    if m%i==0 and n%i==0:
        hcf = i
print(hcf)