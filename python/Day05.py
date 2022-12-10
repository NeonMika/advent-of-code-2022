import re
import Helper


def star01(test):
    stack_data = Helper.readData(
        day=5,
        star=-1 if test else 1,
        text_converter=lambda text: str.split(text, "\n\n")[0],
        line_converter=lambda line: list(line)[1::4]
    )
    move_data = Helper.readData(
        day=5,
        star=-1 if test else 1,
        text_converter=lambda text: str.split(text, "\n\n")[1],
        line_converter=lambda line: [int(x) for x in re.findall("\d+", line)]
    )
    stacks = []
    for _ in range(len(stack_data[0])):
        stacks.append([])
    for line in reversed(stack_data[:-1]):
        for i, stack in enumerate(stacks):
            if line[i] != ' ':
                stack.append(line[i])

    for amount, f, t in move_data:
        for _ in range(amount):
            # pop last element from stacks[f] and append to stacks[t]
            stacks[t-1].append(stacks[f-1].pop())

    res = ''.join(stack[-1] for stack in stacks)
    print("result:", res)


def star02(test):
    stack_data = Helper.readData(
        day=5,
        star=-2 if test else 2,
        text_converter=lambda text: str.split(text, "\n\n")[0],
        line_converter=lambda line: list(line)[1::4]
    )
    move_data = Helper.readData(
        day=5,
        star=-2 if test else 2,
        text_converter=lambda text: str.split(text, "\n\n")[1],
        line_converter=lambda line: [int(x) for x in re.findall("\d+", line)]
    )
    stacks = []
    for _ in range(len(stack_data[0])):
        stacks.append([])
    for line in reversed(stack_data[:-1]):
        for i, stack in enumerate(stacks):
            if line[i] != ' ':
                stack.append(line[i])

    for amount, f, t in move_data:
        stacks[t-1].extend(stacks[f-1][(-amount):])
        del stacks[f-1][(-amount):]

    res = ''.join(stack[-1] for stack in stacks)
    print("result:", res)


star01(True)
star01(False)
star02(True)
star02(False)
