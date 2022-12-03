data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
groups = list(zip(*[iter(data)] * n))
print(groups)