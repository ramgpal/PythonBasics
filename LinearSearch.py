#LinearSearch
def linearSearch(list, key):
    for i in range(len(list)):
        if (list[i] == key):
            return True
        
    return False
list = [1, 2, 3, 4, 5]
key = 4
if(linearSearch(list, key)):
    print("Found")
else:
    print("Not found")