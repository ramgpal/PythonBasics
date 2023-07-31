def selectionSort(list):
    for i in range (len(list)-1):
        tmp = i
        for j in range(i+1, len(list)):
            if(list[tmp] > list[j]):
                tmp = j
        temp = list[tmp]
        list[tmp] = list[i]
        list[i] = temp
def printList(list):
    for i in range(len(list)):
        print(list[i], end=" ")
list = [9, 6, 2, 5, 8]
selectionSort(list)
printList(list)