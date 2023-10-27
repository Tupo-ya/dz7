from functools import reduce

max_num = lambda x, y: x if x > y else y
arr = [1,52,3,4,2,1]
print(reduce(max_num, arr))