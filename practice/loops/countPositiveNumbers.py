num = [1,2,-2,3,3,4,-4,5,-5]
positiveNumCount = 0

for n in num:
    if n > 0:
        positiveNumCount +=1
    print(n)
print("final count = ",positiveNumCount)