i = 1
while(i<11):
    print(i*"*")
    i += 1


for item in range(5):
    print(item+1)

    # List - Collection of items

marks = [95, 98, 99]
print(marks[2])
print(marks[-2])   # - last se index dekhta hai
print(marks[1:3]) # index 1 se 3 tak ke sare element, ending index is excluding

for score in marks:
    print(marks)
marks.append(100)
print(marks)

# to check a number is exist in list or not
print(99 in marks)

# length of the list
print(len(marks))

# to empty list
marks.clear()
print(marks)

