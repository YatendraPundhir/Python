#------------------------------MAP-----------------------------
#num = [2,3,5,6,76,3,3,2]
#square = list(map(lambda x: x*x, num))
#print(square)

#--------------------------FILTER------------------------------
#list_1 = [1,2,3,4,5,6,7,8,9]

#def is_greater_5(num):
#     return num>5

#gr_than_5 = list(filter(is_greater_5, list_1))
#print(gr_than_5)

 #-------------------------REDUCE--------------------------------
from functools import reduce

list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x*y, list1)
print(num)