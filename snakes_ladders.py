import os
import random

import numpy as np


def check_lists(ls1: list, ls2: list):
    # First, check if both lists have the same length
    if len(ls1) != len(ls2):
        return False

    # Check if all items in the lists are the same
    return all(x == y for x, y in zip(ls1, ls2))


def print_matrix(matrix, col, row):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            flg = 0
            if check_lists(col, row) and i == col[0] and j == row[0]:
                print('|'.join(f"p{i + 1}" for i in range(len(col))), end=" ")
            else:
                idx = 0
                for c, r in zip(col, row):
                    idx += 1
                    if i == c and j == r:
                        flg = 1
                        print(f"p{idx}", end="  ")
            if flg == 0:
                print(matrix[i][j], end="   ")
        print()
    print()
    print()


def start_game():
    players = 4
    boards = 6
    matrix: list = [[0] * boards] * boards
    # matrix: list = [
    #     [0, 0, 0, 0, 0, 0],
    # ]

    row: list = [0] * players
    col: list = [0] * players
    index = -1
    print_matrix(matrix, col, row)
    while True:
        if index == players - 1:
            index = 0
        else:
            index += 1
        input_val = input(f"player {index + 1}:")
        val = random.randint(1, 4)
        print(f"Dice Value: {val}")

        if input_val == "0": break
        flag = len(matrix) - 1
        if col[index] == flag and row[index] == 0:
            print("Game end")
            break
        if col[index] == flag and val > row[index]:
            print_matrix(matrix, col, row)
            continue
        if col[index] % 2 == 0:
            if (row[index] + val) > flag:
                fstep = abs(row[index] - flag)
                temp_step = val - fstep

                row[index] += fstep
                col[index] += 1
                row[index] -= (temp_step - 1)
            else:
                row[index] += val
        else:
            if row[index] < val:
                temp_step = abs(row[index] - val)
                row[index] = (temp_step - 1)
                col[index] += 1
            else:
                row[index] -= val
        print_matrix(matrix, col, row)


if __name__ == '__main__':
    start_game()
