def mergeSort(list, si, ei):
    if si >= ei:
        return
    mid = (si + ei) // 2
    mergeSort(list, si, mid)
    mergeSort(list, mid + 1, ei)
    merge(list, mid, si, ei)

def merge(list, mid, si, ei):
    temp = []
    i = si
    j = mid + 1
    while i <= mid and j <= ei:
        if list[i] < list[j]:
            temp.append(list[i])
            i += 1
        else:
            temp.append(list[j])
            j += 1

    while i <= mid:
        temp.append(list[i])
        i += 1

    while j <= ei:
        temp.append(list[j])
        j += 1

    i = si
    for item in temp:
        list[i] = item
        i += 1

def printList(list):
    for i in range(len(list)):
        print(list[i], end=" ")

list = [6, 3, 9, 5, 2, 8]
si = 0
ei = len(list) - 1
mergeSort(list, si, ei)
printList(list)
