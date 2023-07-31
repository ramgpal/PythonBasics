def binarySearch(list, key):
    first = 0
    last = len(list) - 1
    while first <= last:  # Changed from 'while(first < last)' to 'while first <= last'
        mid = (first + last) // 2  # Use floor division '//' to get integer value
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            first = mid + 1
        else:
            last = mid - 1
    return -1  # Return -1 if the key is not found in the list

list = [1, 2, 3, 4, 5]
key = 3
print(binarySearch(list, key))
