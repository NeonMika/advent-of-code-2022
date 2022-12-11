import Helper
import timeit


def star01(test):
    data = Helper.readData(day=XX, test=test, line_converter=lambda line: line)

    print(data)


def star02(test):
    data = Helper.readData(day=XX, test=test, line_converter=lambda line: line)

    print(data)


print()
print("|----------------------------------------|")
print("|--- Test 1 -----------------------------|")
print("|----------------------------------------|")
print()
print("test1 seconds:", timeit.timeit(lambda: star01(True), number=1))
print()
print("|----------------------------------------|")
print("|--- Star 1 -----------------------------|")
print("|----------------------------------------|")
print()
# print("star2 seconds:", timeit.timeit(lambda: star01(False), number=1))
print()
print("|----------------------------------------|")
print("|--- Test 2 -----------------------------|")
print("|----------------------------------------|")
print()
# print("test2 seconds:", timeit.timeit(lambda: star02(True), number=1))
print()
print("|----------------------------------------|")
print("|--- Star 2 -----------------------------|")
print("|----------------------------------------|")
print()
# print("star2 seconds:", timeit.timeit(lambda: star02(False), number=1))
