# from collections import defaultdict
# import sys
#
# def small_box(i, j):
#     col = j//3
#     row = i//3 * 3
#     return box[(row, col)]
#
# sudoku = [list(map(int, input().split())) for _ in range(9)]
#
# box = {(0, 0): 0, (0, 1): 1, (0, 2): 2,
#        (3, 0): 3, (3, 1): 4, (3, 2): 5,
#        (6, 0): 6, (6, 1): 7, (6, 2): 8,}
#
# rows = defaultdict(list)
# columns = defaultdict(list)
# boxs = defaultdict(list)
#
# for i in range(9):
#     for j in range(9):
#         if sudoku[i][j] > 0:
#             rows[i].append(sudoku[i][j])
#             columns[j].append(sudoku[i][j])
#             boxs[small_box(i, j)].append(sudoku[i][j])
#
#
# def is_valid(i, j, k):
#     if k in rows[i] or k in columns[j] or k in boxs[small_box(i, j)]:
#         return False
#     return True
#
# def dfs(i, j):
#     if i > 8 or j > 8:
#         for i in range(9):
#             for j in range(9):
#                 print(f'{sudoku[i][j]}', end=' ')
#             print()
#         sys.exit(0)
#     else:
#         if sudoku[i][j] == 0:
#             for k in range(1, 10):
#                 sudoku[i][j] = k
#                 if is_valid(i, j, k):
#                     rows[i].append(k)
#                     columns[j].append(k)
#                     boxs[small_box(i, j)].append(k)
#
#                     if j < 8:
#                         dfs(i, j+1)
#                     else:
#                         dfs(i+1, 0)
#
#                     rows[i].remove(k)
#                     columns[j].remove(k)
#                     boxs[small_box(i, j)].remove(k)
#                     sudoku[i][j] = 0
#
#                 else:
#                     sudoku[i][j] = 0
#
#         else:
#             if j < 8:
#                 dfs(i, j + 1)
#
#             else:
#                 dfs(i + 1, 0)
#
# dfs(0, 0)


# -------------------------------------------------------------------------------------------------------------------- #

from collections import defaultdict
import sys

def small_box(i, j):
    col = j//3
    row = i//3 * 3
    return box[(row, col)]

sudoku = [list(map(int, input().split())) for _ in range(9)]

box = {(0, 0): 0, (0, 1): 1, (0, 2): 2,
       (3, 0): 3, (3, 1): 4, (3, 2): 5,
       (6, 0): 6, (6, 1): 7, (6, 2): 8,}

rows = defaultdict(set)
columns = defaultdict(set)
boxs = defaultdict(set)

for i in range(9):
    for j in range(9):
        if sudoku[i][j] > 0:
            rows[i].add(sudoku[i][j])
            columns[j].add(sudoku[i][j])
            boxs[small_box(i, j)].add(sudoku[i][j])

def dfs(i, j):
    if i > 8 or j > 8:
        for i in range(9):
            for j in range(9):
                print(f'{sudoku[i][j]}', end=' ')
            print()
        sys.exit(0)
    else:
        if sudoku[i][j] == 0:
            tmp = set(range(1, 10)) - (rows[i] | columns[j] | boxs[small_box(i, j)])
            for k in tmp:
                sudoku[i][j] = k
                rows[i].add(k)
                columns[j].add(k)
                boxs[small_box(i, j)].add(k)

                if j < 8:
                    dfs(i, j+1)
                else:
                    dfs(i+1, 0)

                rows[i].remove(k)
                columns[j].remove(k)
                boxs[small_box(i, j)].remove(k)
                sudoku[i][j] = 0

        else:
            if j < 8:
                dfs(i, j + 1)

            else:
                dfs(i + 1, 0)

dfs(0, 0)