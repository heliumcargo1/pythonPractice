items = ["apple","ball","cat","cat","dog"]
uniqueItem = set()

for i in items:
    if i in uniqueItem:
        print("dublicate item = ",i)
    else:
        uniqueItem.add(i)
print("uniqueItem =  ",uniqueItem)