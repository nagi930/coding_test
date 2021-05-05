import random
from collections import deque
from copy import deepcopy
import turtle


def under60p(board):
    cnt = 0
    for i in range(A):
        for j in range(A):
            if board[i][j] == 'X' or board[i][j] == 'V':
                cnt += 1
    if cnt/A**2 < 0.6:
        return True
    else:
        return False

def draw(board):
    X.clear()
    V.clear()
    N.clear()
    O.clear()
    top = 520
    left = -800
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'X':
                x = left + (col * 10)
                y = top - (row * 10)
                X.goto(x, y)
                X.stamp()
            elif board[row][col] == 'V':
                x = left + (col * 10)
                y = top - (row * 10)
                V.goto(x, y)
                V.stamp()
            elif board[row][col] == 'N':
                x = left + (col * 10)
                y = top - (row * 10)
                N.goto(x, y)
                N.stamp()

            else:
                x = left + (col * 10)
                y = top - (row * 10)
                O.goto(x, y)
                O.stamp()


if __name__ == '__main__':

    turtle.delay(0)
    turtle.ht()
    turtle.tracer(0, 0)

    X = turtle.Turtle()
    X.shapesize(0.3, 0.3, 1)
    X.hideturtle()
    X.penup()
    X.shape('square')
    X.color('green')
    X.speed(0)
    X.setundobuffer(None)

    N = turtle.Turtle()
    N.shapesize(0.3, 0.3, 1)
    N.hideturtle()
    N.penup()
    N.shape('square')
    N.color('red')
    N.speed(0)
    N.setundobuffer(None)

    V = turtle.Turtle()
    V.shapesize(0.3, 0.3, 1)
    V.hideturtle()
    V.penup()
    V.shape('square')
    V.color('purple')
    V.speed(0)
    V.setundobuffer(None)

    O = turtle.Turtle()
    O.shapesize(0.3, 0.3, 1)
    O.hideturtle()
    O.penup()
    O.shape('square')
    O.color('white')
    O.speed(0)
    O.setundobuffer(None)

    screen = turtle.Screen()
    screen.tracer(False)
    screen.bgcolor('black')
    screen.setup(width=1.0, height=1.0)

    A, B = 100, 100

    board = [['O'] * A for _ in range(A)]
    check = [['O'] * A for _ in range(A)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    total = 0
    neutral = 0
    draw(board)

    while under60p(board):
        for i in range(A):
            for j in range(A):
                if board[i][j] == 'N':
                    board[i][j] = 'X'
        screen.update()
        cnt = B
        while cnt > 0:
            row = random.randint(0, A-1)
            col = random.randint(0, A-1)
            if board[row][col] == 'O':
                board[row][col] = 'N'
                cnt -= 1
        total += 1

        draw(board)

        check = deepcopy(board)
        zero_count = []
        queue = deque()
        for i in range(A):
            for j in range(A):
                if check[i][j] == 'O':
                    all = []
                    check[i][j] = 'X'
                    queue.append((i, j))
                    all.append((i, j))
                    while queue:
                        temp = queue.popleft()
                        for d in range(4):
                            x = temp[1] + dx[d]
                            y = temp[0] + dy[d]
                            if 0<= x <= A-1 and 0<= y <= A-1 and check[y][x] == 'O':
                                check[y][x] = 'X'
                                queue.append((y, x))
                                all.append((y, x))
                    zero_count.append(all)


        if len(zero_count) < 2:
            continue
        else:
            zero_count.sort(key=len)
            for zeros in zero_count[:-1]:

                if len(zeros) == 1:
                    for row, col in zeros:
                        board[row][col] = 'V'
                        neutral += 1
                else:
                    for row, col in zeros:
                        board[row][col] = 'V'
                        neutral += 1
        draw(board)
    screen.mainloop()
