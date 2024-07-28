alist = [[1,2,3],[4],[5,6,7]]
flatlist = []

for sublist in alist:
    for element in sublist:
        flatlist.append(element)
print(flatlist)
