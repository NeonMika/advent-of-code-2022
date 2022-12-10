import Helper


def star01(test):
    startOfCycle = 1
    register = 1
    signal_sum = 0
    data = Helper.readData(day=10, test=test)

    def incCycle():
        nonlocal startOfCycle
        nonlocal signal_sum
        # print("during cycle", startOfCycle, "register", register)
        if startOfCycle in (20, 60, 100, 140, 180, 220):
            signal_sum += startOfCycle * register
        startOfCycle += 1

    for d in data:
        if d[0] == "noop":
            incCycle()
        elif d[0] == "addx":
            incCycle()
            incCycle()
            register += int(d[1])

    print("signal_sum", signal_sum)


def star02(test):
    startOfCycle = 1
    register = 1
    signal_sum = 0
    data = Helper.readData(day=10, test=test)

    def incCycle():
        nonlocal startOfCycle
        nonlocal signal_sum

        pixel = (startOfCycle - 1) % 40

        print(
            "#" if pixel in (register - 1, register, register + 1) else ".",
            end="",
        )
        if startOfCycle in (40, 80, 120, 160, 200, 240):
            print()
        startOfCycle += 1

    for d in data:
        if d[0] == "noop":
            incCycle()
        elif d[0] == "addx":
            incCycle()
            incCycle()
            register += int(d[1])


print()
print("|----------------------------------------|")
print("|--- Test 1 -----------------------------|")
print("|----------------------------------------|")
print()
star01(True)
print()
print("|----------------------------------------|")
print("|--- Star 1 -----------------------------|")
print("|----------------------------------------|")
print()
star01(False)
print()
print("|----------------------------------------|")
print("|--- Test 2 -----------------------------|")
print("|----------------------------------------|")
print()
star02(True)
print()
print("|----------------------------------------|")
print("|--- Star 2 -----------------------------|")
print("|----------------------------------------|")
print()
star02(False)
