nums = [int(i) for i in range(1, 100)]
is_nada = lambda x: (x % 19 == 0) or (x % 13 == 0)

print(list(filter(is_nada, nums)))