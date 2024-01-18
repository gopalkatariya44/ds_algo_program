from set_matrix_zero import print_matrix


def rotate_matrix_ap1(matrix):
    mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    n = (len(matrix) - 1)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            mat[y][n - x] = matrix[x][y]


def rotate_matrix_ap2(matrix):
    print_matrix(matrix)
    for x in range(len(matrix)):
        for y in range(x, len(matrix[x])):
            matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]
        matrix[x] = matrix[x][::-1]
    print_matrix(matrix)
 

if __name__ == '__main__':
    # matrix = [[1, 2, 3, 4],
    #           [5, 6, 7, 8],
    #           [9, 10, 11, 12],
    #           [13, 14, 15, 16]]
    matrix = [[1, 2, 3],  # 7, 4, 1
              [4, 5, 6],  # 8, 5, 2
              [7, 8, 9]]  # 9, 6, 3
    # matrix = [[1, 1, 1, 1, 0],
    #           [1, 1, 0, 1, 1],
    #           [1, 1, 1, 1, 1],
    #           [1, 1, 0, 1, 1],
    #           [1, 1, 1, 1, 1]]
    rotate_matrix_ap2(matrix)
