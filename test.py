from operator import itemgetter

list=[[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list.sort(key=itemgetter(1,2), reverse=False)
print(list)