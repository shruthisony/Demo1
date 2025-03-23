l1 = [1,17,10,4]
l2 = [5,6,18,20]
l3 = []

for i in range(len(l1)):
    l3.append(max(l1[i]))

for i in range(len(l2)):
    l3.append(max(l2[i]))


print(l3)