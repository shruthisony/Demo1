l1 = [1, 17, 10, 4]
l2 = [5, 6, 18, 20]

max_elements = []
for i in range(len(l1)):
    max_elements.append(max(l1[i], l2[i]))

print(max_elements)