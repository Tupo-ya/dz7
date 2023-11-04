sum_nums = lambda x, y: x+y
ravn_arr = lambda arr1, arr2: (arr1 + [0] * (len(arr2)-len(arr1))) if len(arr1) < len(arr2) else arr1

arr1 = [1, 3, 5]
arr2 = [1, 7, 2, 9]

arr1 = ravn_arr(arr1, arr2)
arr2 = ravn_arr(arr2, arr1)

print(list(map(sum_nums, arr1, arr2)))