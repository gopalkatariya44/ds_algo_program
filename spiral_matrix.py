def spiral_matrix(matrix):
    ans = []
    top, bot = 0, len(matrix) - 1
    left, right = 0, len(matrix) - 1
    while top <= bot and left <= right:
        for i in range(left, right + 1):
            print(i, end="")
            ans.append(matrix[top][i])
        print()
        top += 1
        for i in range(top, bot + 1):
            print(i, end="")
            ans.append(matrix[i][right])
        print()
        right -= 1
        for i in range(right, left, -1):
            print(i, end="")
            ans.append(matrix[bot][i]) 
        print()
        bot -= 1
        for i in range(bot + 1, top - 1, -1):
            print(i, end="")
            ans.append(matrix[i][left])
        print()
        left += 1
    print(ans)


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4, 5, 6],
        [20, 21, 22, 23, 24, 7],
        [19, 32, 33, 34, 25, 8],
        [18, 31, 36, 35, 26, 9],
        [17, 30, 29, 28, 27, 10],
        [16, 15, 14, 13, 12, 11],
    ]
    # matrix = [
    #     [1, 2, 3, 4],
    #     [12, 13, 14, 5],
    #     [11, 16, 15, 6],
    #     [10, 9, 8, 7],
    # ]
    spiral_matrix(matrix)
