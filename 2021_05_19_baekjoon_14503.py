# https://www.acmicpc.net/problem/14503

class Robot:
    clean_cnt = 0
    cardinal = [(0, -1, 0), (1, 0, 1), (2, 1, 0), (3, 0, -1)]

    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d

    def __str__(self):
        for i in range(n):
            for j in range(m):
                print(board[i][j], end='')
            print()
        return f'position: ({self.r}, {self.c})'

    def clean(self):
        if board[self.r][self.c] == 0:
            board[self.r][self.c] = 2
            Robot.clean_cnt += 1

    def search1(self):
        if self.check_left():
            d, dr, dc = Robot.cardinal[self.d-1]
            self.d = d
            self.r += dr
            self.c += dc
            return True
        return False

    def search2(self):
        if not self.check_left():
            d, _, _ = Robot.cardinal[self.d-1]
            self.d = d
            return True
        return False

    def search3(self):
        if self.check_all() and self.check_backward():
            _, dr, dc = Robot.cardinal[self.d-2]
            self.r += dr
            self.c += dc
            return True
        return False

    def search4(self):
        if self.check_all() and not self.check_backward():
            return True
        return False

    def check_left(self):
        _, dr, dc = Robot.cardinal[self.d-1]
        if board[self.r + dr][self.c + dc] == 0:
            return True
        else:
            return False

    def check_all(self):
        for i in range(4):
            _, dr, dc = Robot.cardinal[i]
            if board[self.r + dr][self.c + dc] == 0:
                return False
        return True

    def check_backward(self):
        _, dr, dc = Robot.cardinal[self.d-2]
        if board[self.r + dr][self.c + dc] != 1:
            return True
        return False

    def run(self):
        while True:
            self.clean()
            if self.search4():
                break
            if self.search3():
                continue
            if self.search1():
                self.clean()
                continue
            if self.search2():
                continue


if __name__ == '__main__':
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    robot = Robot(r, c, d)
    robot.run()
    print(robot.clean_cnt)
