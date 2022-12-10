import dataclasses
import Helper
import abc


@dataclasses.dataclass
class Item(abc.ABC):
    name: str
    parent: "Item" | None = None

    @abc.abstractmethod
    def get_size(self) -> int:
        pass


@dataclasses.dataclass(frozen=False)
class Directory(Item):
    children: dict[str, Item] = dataclasses.field(default_factory=dict)

    def get_size(self):
        return sum(child.get_size() for child in self.children.values())


@dataclasses.dataclass
class File(Item):
    size: int = 0

    def get_size(self):
        return self.size


def star01(test):
    data = Helper.readData(day=7, test=test)[1:]

    root = Directory("/")
    curr = root
    directories = [root]

    for line in data:
        if line[1] == "cd":
            if line[2] == "..":
                curr = curr.parent
            else:
                curr = curr.children[line[2]]
        elif line[1] == "ls":
            continue
        else:
            if line[0] == "dir":
                x = Directory(line[1], curr)
                curr.children[line[1]] = x
                directories.append(x)
            else:
                curr.children[line[1]] = File(line[1], curr, int(line[0]))

    result = sum(dir.get_size() for dir in directories if dir.get_size() <= 100000)
    print("sum", result)


def star02(test):
    data = Helper.readData(day=7, test=test)[1:]

    root = Directory("/")
    curr = root
    directories = [root]

    for line in data:
        if line[1] == "cd":
            if line[2] == "..":
                curr = curr.parent
            else:
                curr = curr.children[line[2]]
        elif line[1] == "ls":
            continue
        else:
            if line[0] == "dir":
                x = Directory(line[1], curr)
                curr.children[line[1]] = x
                directories.append(x)
            else:
                curr.children[line[1]] = File(line[1], curr, int(line[0]))

    free = 70000000 - root.get_size()
    missing = 30000000 - free

    result = sorted(dir.get_size() for dir in directories if dir.get_size() >= missing)[
        0
    ]

    print("Size of dir to delete:", result)


star01(True)
star01(False)
star02(True)
star02(False)
