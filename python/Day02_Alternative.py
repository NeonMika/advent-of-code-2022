import dataclasses
import Helper

# Left: A for Rock, B for Paper, and C for Scissors
# Right: X for Rock, Y for Paper, and Z for Scissors

# Shape score: 1 for Rock, 2 for Paper, and 3 for Scissors
# Result score: 0 if you lost, 3 if the round was a draw, and 6 if you won

A = "A"
B = "B"
C = "C"
X = "X"
Y = "Y"
Z = "Z"
R = "R"
P = "P"
S = "S"

DRAW = "DRAW"
LOSE = "LOSE"
WIN = "WIN"

M = {
    (R, R): 3+1, (R, P): 6+2, (R, S): 0+3,
    (P, R): 0+1, (P, P): 3+2, (P, S): 6+3,
    (S, R): 6+1, (S, P): 0+2, (S, S): 3+3,
}

M2 = {
    (R, LOSE): 0+3, (R, DRAW): 3+1, (R, WIN): 6+2,
    (P, LOSE): 0+1, (P, DRAW): 3+2, (P, WIN): 6+3,
    (S, LOSE): 0+2, (S, DRAW): 3+3, (S, WIN): 6+1,
}

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.


def star01(test):
    data = Helper.readData(
        day=2,
        star=-1 if test else 1,
        text_converter=lambda text: text.replace(A, R).replace(X, R).replace(B, P).replace(Y, P).replace(C, S).replace(Z, S),
        line_converter=lambda line: M[tuple(line.split())]
    )
    print(sum(data))


def star02(test):
    data = Helper.readData(
        day=2,
        star=-1 if test else 1,
        text_converter=lambda text: text.replace(A, R).replace(B, P).replace(C, S).replace(X, LOSE).replace(Y, DRAW).replace(Z, WIN),
        line_converter=lambda line: M2[tuple(line.split())]
    )
    print(sum(data))


star01(True)
star01(False)
star02(True)
star02(False)
