def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end='  ')
        print()
    print()

def set_matrix_zero(matrix):
    print_matrix(matrix)
    # row = []
    # column = []
    col0 = 1
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 0:
                matrix[x][0] = 0
                if y != 0:
                    matrix[0][y] = 0
                else:
                    col0 = 0
                # row.append(x)
                # column.append(y)

    # row = list(set(row))
    # column = list(set(column))
    # print(row, column)
    print(col0)
    print_matrix(matrix)
    for x in range(1, len(matrix)):
        for y in range(1, len(matrix[x])):
            if matrix[0][y] == 0 or matrix[x][0] == 0:
                matrix[x][y] = 0

    if matrix[0][0] == 0:
        for y in range(len(matrix)):
            matrix[0][y] = 0

    if col0 == 0:
        for x in range(len(matrix)):
            matrix[x][0] = 0

    print('---')
    print_matrix(matrix)
    print('--------------')


if __name__ == '__main__':
    matrix = [[1, 1, 1, 0],
              [1, 1, 1, 1],
              [0, 1, 0, 1],
              [1, 1, 1, 0]]
    set_matrix_zero(matrix)
    matrix = [[1, 1, 1, 1, 0],
              [1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1]]
    set_matrix_zero(matrix)
