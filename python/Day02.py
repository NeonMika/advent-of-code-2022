import dataclasses
import Helper

# Left: A for Rock, B for Paper, and C for Scissors
# Right: X for Rock, Y for Paper, and Z for Scissors

# Shape score: 1 for Rock, 2 for Paper, and 3 for Scissors
# Result score: 0 if you lost, 3 if the round was a draw, and 6 if you won


@dataclasses.dataclass
class Move:
    name: str
    left: str
    right: str
    score: int

    def __init__(self, name, left, right, score):
        self.name = name
        self.left = left
        self.right = right
        self.score = score


R = "Rock"
P = "Paper"
S = "Scissors"


MOVES = [
    Move(R, "A", "X", 1),
    Move(P, "B", "Y", 2),
    Move(S, "C", "Z", 3)
]
MOVES_BY_LEFT = {move.left: move for move in MOVES}
MOVES_BY_RIGHT_STAR1 = {move.right: move for move in MOVES}
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
MOVES_BY_NAME = {move.name: move for move in MOVES}
RESPONSE_MOVES_STAR2 = {
    (R, "X"): MOVES_BY_NAME[S], (R, "Y"): MOVES_BY_NAME[R], (R, "Z"): MOVES_BY_NAME[P],
    (P, "X"): MOVES_BY_NAME[R], (P, "Y"): MOVES_BY_NAME[P], (P, "Z"): MOVES_BY_NAME[S],
    (S, "X"): MOVES_BY_NAME[P], (S, "Y"): MOVES_BY_NAME[S], (S, "Z"): MOVES_BY_NAME[R]
}


WINS = ((S, P), (P, R), (R, S))
LOSES = [(y, x) for x, y in WINS]


@dataclasses.dataclass
class Entry:
    enemy: Move
    my: Move

    def __init__(self, enemy, my):
        self.enemy = enemy
        self.my = my

    def score(self):
        combi = (self.my.name, self.enemy.name)
        is_win = combi in WINS
        is_loss = combi in LOSES
        is_draw = not is_win and not is_loss

        return self.my.score + (6 if is_win else (3 if is_draw else 0))


def star01(test):
    def line_converter(line: str):
        left, right = line.split()
        return Entry(MOVES_BY_LEFT[left], MOVES_BY_RIGHT_STAR1[right])
    data = Helper.readData(day=2, star=-1 if test else 1, line_converter=line_converter)
    print(sum(entry.score() for entry in data))


def star02(test):
    def line_converter(line: str):
        left, right = line.split()
        left_move = MOVES_BY_LEFT[left]
        right_move = RESPONSE_MOVES_STAR2[(left_move.name, right)]
        return Entry(left_move, right_move)
    data = Helper.readData(day=2, star=-2 if test else 2, line_converter=line_converter)
    print(sum(entry.score() for entry in data))


star01(True)
star01(False)
star02(True)
star02(False)
