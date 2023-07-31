thisDict = {
    "Name": "Ram",
    "Age": 19,
    "Occuption": "Student"
}
print(thisDict)
#Acess the item from dictionary
print(thisDict.get("Age"))
#add  item in dictionaries
thisDict["Roll Number"] = 2101921520142
print(thisDict)
#copy method
newDict = thisDict.copy()
print(newDict)
# clear() method
print(thisDict.clear())
